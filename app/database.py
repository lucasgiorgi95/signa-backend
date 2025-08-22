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
    # Obtener la ruta de la base de datos de las variables de entorno
    db_path = os.getenv('DATABASE_URL', '/data/marcas.db')
    
    # Convertir a ruta absoluta
    db_path = str(Path(db_path).absolute())
    
    # Asegurarse de que el directorio existe
    try:
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        # Dar permisos al directorio
        os.chmod(os.path.dirname(db_path), 0o777)
    except Exception as e:
        print(f"Advertencia: No se pudo configurar el directorio de la base de datos: {e}")
    
    # Asegurarse de que la ruta empieza con 3 barras para rutas absolutas en SQLite
    if not db_path.startswith('sqlite:'):
        if db_path.startswith('/'):
            return f'sqlite://{db_path}'
        return f'sqlite:///{db_path}'
    return db_path

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
