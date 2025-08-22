import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cargar variables de entorno
load_dotenv()

# Obtener la ruta de la base de datos
def get_database_url():
    # Obtener la URL de la base de datos de las variables de entorno
    database_url = os.getenv('DATABASE_URL', 'sqlite:///./marcas.db')
    
    # Si ya es una URL completa de SQLite, extraer solo la ruta del archivo
    if database_url.startswith('sqlite:///'):
        db_file_path = database_url.replace('sqlite:///', '')
        
        # Si es una ruta relativa (empieza con ./), convertir a absoluta
        if db_file_path.startswith('./'):
            db_file_path = os.path.abspath(db_file_path)
        
        # Asegurarse de que el directorio existe
        db_dir = os.path.dirname(db_file_path)
        if db_dir:  # Solo si hay un directorio
            try:
                os.makedirs(db_dir, exist_ok=True)
            except Exception as e:
                print(f"Advertencia: No se pudo crear el directorio de la base de datos: {e}")
        
        # Retornar la URL completa
        return f'sqlite:///{db_file_path}'
    
    return database_url

# Configurar la URL de la base de datos
SQLALCHEMY_DATABASE_URL = get_database_url()

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
