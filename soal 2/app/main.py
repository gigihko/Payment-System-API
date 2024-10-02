from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# Konfigurasi hashing untuk PIN
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 password flow setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Konfigurasi JWT
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")  # Ganti dengan kunci rahasia yang lebih aman
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7


class UserRegister(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    address: str
    pin: str

class UserLogin(BaseModel):
    phone_number: str
    pin: str

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict):
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/register/")
async def register(user: UserRegister, db: db_dependency):
    # Cek apakah nomor telepon sudah terdaftar
    existing_user = db.query(models.User).filter(models.User.phone_number == user.phone_number).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone Number already registered")

    # Hash PIN sebelum disimpan
    hashed_pin = pwd_context.hash(user.pin)

    # Simpan pengguna baru ke dalam database
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        phone_number=user.phone_number,
        address=user.address,
        pin=hashed_pin
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
        "status": "SUCCESS",
        "result": {
            "user_id": db_user.id,
            "first_name": db_user.first_name,
            "last_name": db_user.last_name,
            "phone_number": db_user.phone_number,
            "address": db_user.address,
        }
    }

@app.post("/login/")
async def login(user: UserLogin, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.phone_number == user.phone_number).first()
    
    if not db_user or not pwd_context.verify(user.pin, db_user.pin):  # Verifikasi PIN
        raise HTTPException(status_code=400, detail="Phone Number and PIN doesn’t match.")
    
    access_token = create_access_token(data={"sub": db_user.phone_number})
    refresh_token = create_refresh_token(data={"sub": db_user.phone_number})

    # Simpan refresh token ke database
    db_user.refresh_token = refresh_token
    db.commit()  # Simpan perubahan ke database

    return {
        "status": "SUCCESS",
        "result": {
            "access_token": access_token,
            "refresh_token": refresh_token,  # Tambahkan refresh token ke response
        }
    }

# Model untuk request top-up
class TopUpRequest(BaseModel):
    amount: float

# Endpoint untuk top-up
@app.post("/topup/")
async def top_up(top_up_data: TopUpRequest, db: db_dependency, token: Annotated[str, Depends(oauth2_scheme)]):
    # Decode JWT untuk mendapatkan nomor telepon pengguna
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        phone_number = payload.get("sub")
        if phone_number is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    # Cari pengguna berdasarkan nomor telepon
    user = db.query(models.User).filter(models.User.phone_number == phone_number).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Simpan transaksi top-up
    new_topup = models.TopUp(
        user_id=user.id,
        amount=top_up_data.amount,
    )
    db.add(new_topup)

    # Update saldo pengguna
    balance_before = user.balance
    user.balance += top_up_data.amount
    balance_after = user.balance

    # Simpan perubahan ke database
    db.commit()

    return {
        "status": "SUCCESS",
        "result": {
            "top_up_id": new_topup.id,
            "amount_top_up": new_topup.amount,
            "balance_before": balance_before,
            "balance_after": balance_after,
            "created_date": new_topup.created_date,
        }
    }
