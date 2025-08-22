import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cargar variables de entorno
load_dotenv()

# Obtener la ruta de la base de datos de las variables de entorno o usar la predeterminada
DB_PATH = os.getenv('DATABASE_URL', 'sqlite:////app/data/marcas.db')

# Asegurarse de que la URL de la base de datos esté en el formato correcto
if not DB_PATH.startswith('sqlite:'):
    if not DB_PATH.startswith('/'):
        DB_PATH = f'/app/data/{DB_PATH}'
    DB_PATH = f'sqlite:///{DB_PATH}'

# Usar la URL de la base de datos
SQLALCHEMY_DATABASE_URL = DB_PATH

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
