from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app import database as db
import app.crud.crudChequera as crudChequera
import app.schemas.schemaChequera as schemaChequera
from sqlalchemy import exc

from app import services
    
app = FastAPI()

def create_tables():
    try:
        db.engine.connect().execute("SELECT 1 FROM your_table_name LIMIT 1")
    except exc.SQLAlchemyError:
        db.Base.metadata.create_all(bind=db.engine)

create_tables()

@app.post("/api/chequeras/", response_model=schemaChequera.Chequera)
async def create_chequera(
    chequera: schemaChequera.BaseChequera, 
    db: Session = Depends(services.get_db)):
    crudChequera.check_create_conditions(chequera)
    return await crudChequera.create_chequera(db, chequera)

@app.get("/api/chequeras/", response_model=List[schemaChequera.Chequera])
async def get_chequeras(limit: int = 100, db: Session = Depends(services.get_db)):
    chequeras = crudChequera.get_chequeras(db, limit)
    return await chequeras

