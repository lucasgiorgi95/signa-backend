import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cargar variables de entorno
load_dotenv()

# Obtener la URL de la base de datos
def get_database_url():
    database_url = os.getenv('DATABASE_URL')
    
    if not database_url:
        # Fallback para desarrollo local
        return 'sqlite:///./marcas.db'
    
    # Si es PostgreSQL de Render, puede venir con postgres:// que necesita ser postgresql://
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    
    return database_url

# Configurar la URL de la base de datos
SQLALCHEMY_DATABASE_URL = get_database_url()

# Determinar si es SQLite o PostgreSQL
is_sqlite = SQLALCHEMY_DATABASE_URL.startswith('sqlite')

# Configurar el motor según el tipo de base de datos
if is_sqlite:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, 
        connect_args={"check_same_thread": False},
        pool_pre_ping=True
    )
else:
    # PostgreSQL
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        pool_pre_ping=True,
        pool_recycle=300
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
