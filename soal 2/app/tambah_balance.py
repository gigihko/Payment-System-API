from sqlalchemy import create_engine, MetaData, Table, Column, Float, text
from database import engine

# Menginisialisasi metadata
metadata = MetaData()

# Menghubungkan ke tabel users yang sudah ada
users_table = Table('users', metadata, autoload_with=engine)

# Menambahkan kolom balance secara manual
with engine.connect() as conn:
    # Periksa apakah kolom sudah ada
    if not hasattr(users_table.c, 'balance'):
        # Jika kolom balance belum ada, tambahkan
        conn.execute(text('ALTER TABLE users ADD COLUMN balance FLOAT DEFAULT 0.0'))

print("Kolom 'balance' berhasil ditambahkan.")
