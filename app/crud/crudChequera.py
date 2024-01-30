from app import database as db
from fastapi import HTTPException
from sqlalchemy.orm import Session
import app.models.modelChequera as modelChequera
import app.schemas.schemaChequera as schemaChequera
from sqlalchemy import exc

async def create_chequera(
        db: Session, 
        chequera: schemaChequera.BaseChequera ) -> schemaChequera.Chequera:
    chequera = modelChequera.Chequera(**chequera.model_dump())
    db.add(chequera)
    db.commit()
    db.refresh(chequera)
    return schemaChequera.Chequera.model_validate(chequera)

def validate_create_conditions(chequera):
    if chequera.rango_maximo < 0 or chequera.rango_minimo < 0:
        raise HTTPException(status_code=400, detail="rango_maximo and rango_minimo must be greater than 0")
    elif chequera.rango_minimo >= chequera.rango_maximo:
        raise HTTPException(status_code=400, detail="rango_minimo must be smaller than rango_maximo")
    elif chequera.rango_maximo - chequera.rango_minimo > 30:
        raise HTTPException(status_code=400, detail="the difference between rango_maximo and rango_minimo must be smaller than 30")


async def get_chequeras(db: Session, limit: int = 100) -> list[schemaChequera.Chequera]:
    return [schemaChequera.Chequera.model_validate(chequera) for chequera in db.query(modelChequera.Chequera).limit(limit).all()]
