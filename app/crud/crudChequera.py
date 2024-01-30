from fastapi import HTTPException
from sqlalchemy.orm import Session
import app.models.modelChequera as model
import app.schemas.schemaChequera as schema

from app.crud.auxChequera import check_chequera_completa 

async def create_chequera(
        db: Session, 
        chequera: schema.BaseChequera ) -> schema.Chequera:
    chequera = model.Chequera(**chequera.model_dump())
    db.add(chequera)
    db.commit()
    db.refresh(chequera)
    return schema.Chequera.model_validate(chequera)


async def get_chequeras(db: Session, completa: bool, limit: int = 100) -> list[schema.Chequera]:
    chequeras = db.query(model.Chequera).limit(limit).all()
    if completa:
        chequeras = [chequera for chequera in chequeras if check_chequera_completa(chequera)]
    return [schema.Chequera.model_validate(chequera) for chequera in chequeras]


async def get_chequera_id(db: Session, chequera_id: int) -> schema.Chequera:
    chequera = db.query(model.Chequera).filter(model.Chequera.id == chequera_id).first()
    if chequera is None:
        raise HTTPException(status_code=404, detail="Chequera not found")
    return schema.Chequera.model_validate(chequera)


async def update_chequera(db: Session, chequera_id: int, chequera: schema.BaseChequera) -> schema.Chequera:
    chequera_db = db.query(model.Chequera).filter(model.Chequera.id == chequera_id).first()
    if chequera_db is None:
        raise HTTPException(status_code=404, detail="Chequera not found")
    for key, value in chequera.model_dump().items():
        setattr(chequera_db, key, value)
    db.commit()
    db.refresh(chequera_db)
    return schema.Chequera.model_validate(chequera_db)


async def delete_chequera(db: Session, chequera_id: int):
    chequera = db.query(model.Chequera).filter(model.Chequera.id == chequera_id).first()
    if chequera is None:
        raise HTTPException(status_code=404, detail="Chequera not found")
    db.delete(chequera)
    db.commit()
    return {"message": "Chequera deleted"}