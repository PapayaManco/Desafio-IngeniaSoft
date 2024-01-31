from fastapi import Depends,  APIRouter
from typing import List
from sqlalchemy.orm import Session
import app.cruds.crudChequera as crudChequera
import app.schemas.schemaChequera as schemaChequera
from app.cruds.auxChequera import validate_create_chequera
from app import services


router = APIRouter()

responses_dict = {404: {"description": "Chequera no encontrada"}}

@router.post("/api/chequeras/", response_model=schemaChequera.Chequera)
async def create_chequera(chequera: schemaChequera.BaseChequera, db: Session = Depends(services.get_db)):
    validate_create_chequera(chequera)
    return await crudChequera.create_chequera(db, chequera)

@router.get("/api/chequeras/", response_model=List[schemaChequera.Chequera])
async def get_chequeras(completa: bool = False, limit: int = 100, db: Session = Depends(services.get_db)):
    chequeras = crudChequera.get_chequeras(db,completa, limit)
    return await chequeras

@router.get("/api/chequeras/{chequera_id}", response_model=schemaChequera.ChequeraWithCheques, responses= responses_dict)
async def get_chequera(chequera_id: int, db: Session = Depends(services.get_db)):
    return await crudChequera.get_chequera_id(db, chequera_id)

@router.put("/api/chequeras/{chequera_id}", response_model=schemaChequera.ChequeraWithCheques, responses= responses_dict)
async def update_chequera(chequera_id: int, chequera: schemaChequera.UpdateChequera, db: Session = Depends(services.get_db)):
    return await crudChequera.update_chequera(db, chequera_id, chequera)

@router.delete("/api/chequeras/{chequera_id}",  responses= responses_dict)
async def delete_chequera(chequera_id: int, db: Session = Depends(services.get_db)):
    return await crudChequera.delete_chequera(db, chequera_id)