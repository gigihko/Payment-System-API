from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))  # UUID sebagai user_id
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)
    address = Column(String)
    pin = Column(String)  # Pastikan untuk melakukan hashing pin jika diperlukan
    created_date = Column(DateTime, default=datetime.utcnow)  # Menyimpan tanggal pembuatan
    refresh_token = Column(String)  # Kolom untuk menyimpan refresh token
    balance = Column(Float, default=0.0)  # Tambahkan kolom balance, dengan nilai awal 0

class TopUp(Base):
    __tablename__ = "topups"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))  # UUID untuk top_up_id
    user_id = Column(String, nullable=False)  # ID pengguna yang melakukan top up
    amount = Column(Float, nullable=False)  # Jumlah top up
    created_date = Column(DateTime, default=datetime.utcnow)  # Tanggal top up