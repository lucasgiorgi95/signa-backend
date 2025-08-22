import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cargar variables de entorno
load_dotenv()

# Configurar ruta para la base de datos SQLite
# Usamos /app/data/marcas.db para coincidir con la configuración en start.sh
SQLITE_DB_PATH = "/app/data/marcas.db"

# Asegurar que el directorio existe
os.makedirs(os.path.dirname(SQLITE_DB_PATH), exist_ok=True)

# Usar SQLite en todos los entornos
SQLALCHEMY_DATABASE_URL = f"sqlite://{SQLITE_DB_PATH}"

# Configurar el motor de SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},  # Necesario para SQLite
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
