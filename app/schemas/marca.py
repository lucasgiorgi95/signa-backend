from pydantic import BaseModel
from typing import Optional

class MarcaBase(BaseModel):
    
    nombre: str
    descripcion: Optional[str] = None
    dueno: str

class MarcaCreate(MarcaBase):
    
    pass

class MarcaUpdate(BaseModel):
   
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    dueno: Optional[str] = None

class MarcaInDBBase(MarcaBase):
   
    id: int

    class Config:
        from_attributes = True

class Marca(MarcaInDBBase):
    
    pass
