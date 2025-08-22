from sqlalchemy import Column, Integer, String, Text
from ..database import Base

class Marca(Base):
  
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    descripcion = Column(Text, nullable=True)
    dueno = Column(String, index=True, nullable=False)
