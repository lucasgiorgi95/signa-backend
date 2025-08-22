from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.models.marca import Marca as MarcaModel
from ....database import get_db
from ....schemas import marca as schemas

router = APIRouter()

@router.post("/", response_model=schemas.Marca, status_code=201)
def crear_marca(marca_data: schemas.MarcaCreate, db: Session = Depends(get_db)):
    """
    Crea una nueva marca.
    """
    db_marca = MarcaModel(**marca_data.model_dump())
    db.add(db_marca)
    db.commit()
    db.refresh(db_marca)
    return db_marca

@router.get("/", response_model=List[schemas.Marca])
def listar_marcas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtiene una lista de todas las marcas con paginación.
    """
    marcas = db.query(MarcaModel).offset(skip).limit(limit).all()
    return marcas

@router.get("/{marca_id}", response_model=schemas.Marca)
def obtener_marca(marca_id: int, db: Session = Depends(get_db)):
    """
    Obtiene los detalles de una marca por su ID.
    """
    db_marca = db.query(MarcaModel).filter(MarcaModel.id == marca_id).first()
    if db_marca is None:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return db_marca

@router.put("/{marca_id}", response_model=schemas.Marca)
def actualizar_marca(
    marca_id: int, 
    marca_data: schemas.MarcaUpdate, 
    db: Session = Depends(get_db)
):
    """
    Actualiza una marca existente.
    """
    db_marca = db.query(MarcaModel).filter(MarcaModel.id == marca_id).first()
    if db_marca is None:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    
    # Actualizar solo los campos proporcionados
    update_data = marca_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_marca, field, value)
    
    db.commit()
    db.refresh(db_marca)
    return db_marca

@router.delete("/{marca_id}", status_code=204)
def eliminar_marca(marca_id: int, db: Session = Depends(get_db)):
    """
    Elimina una marca por su ID.
    """
    db_marca = db.query(MarcaModel).filter(MarcaModel.id == marca_id).first()
    if db_marca is None:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    
    db.delete(db_marca)
    db.commit()
    return None
