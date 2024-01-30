from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session

import app.crud.crudChequera as crudChequera
from app.schemas.schemaChequera  import Chequera, CreateChequera

from app import database, services
    
app = FastAPI()

crudChequera.create_tables()

@app.post("/api/chequeras/", response_model=Chequera)
async def create_chequera(
    chequera: CreateChequera, 
    db: Session = Depends(services.get_db)):
    return await crudChequera.create_chequera(db=db, chequera=chequera)

@app.get("/api/chequeras/", response_model=List[Chequera])
async def get_chequeras(limit: int = 100, db: Session = Depends(services.get_db)):
    chequeras = crudChequera.get_chequeras(db, limit)
    return await chequeras