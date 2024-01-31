from fastapi import Depends,  APIRouter
from typing import List
from sqlalchemy.orm import Session
import app.cruds.crudCheque as crudCheque
import app.schemas.schemaCheque as schemaCheque
from app.cruds.auxCheque import validate_create_cheque, validate_update_cheque, find_cheque_id
from app import services

router = APIRouter()

responses_dict = {404: {"description": "Chequera no encontrada."}}

@router.post("/api/cheques/", response_model=schemaCheque.Cheque, responses=responses_dict)
async def create_cheque(cheque: schemaCheque.BaseCheque, db: Session = Depends(services.get_db)):
    validate_create_cheque(db, cheque)
    return await crudCheque.create_cheque(db, cheque)

@router.get("/api/cheques/", response_model=List[schemaCheque.Cheque])
async def get_cheques(limit: int = 100, db: Session = Depends(services.get_db)):
    return await crudCheque.get_cheques(db, limit)

@router.put("/api/cheques/{cheque_id}", response_model=schemaCheque.Cheque, responses=responses_dict)
async def update_cheque(cheque_id: int, cheque: schemaCheque.BaseCheque, db: Session = Depends(services.get_db)):
    validate_update_cheque(db, cheque, cheque_id)
    return await crudCheque.update_cheque(db, cheque_id, cheque)

@router.delete("/api/cheques/{cheque_id}", responses=responses_dict)
async def delete_cheque(cheque_id: int, db: Session = Depends(services.get_db)):
    find_cheque_id(db, cheque_id)
    return await crudCheque.delete_cheque(db, cheque_id)