from app import database
from sqlalchemy.orm import Session
from app.models.modelChequera import Chequera
from app.schemas.schemaChequera import CreateChequera
from sqlalchemy import exc

def create_tables():
    try:
        database.engine.connect().execute("SELECT 1 FROM your_table_name LIMIT 1")
    except exc.SQLAlchemyError:
        database.Base.metadata.create_all(bind=database.engine)

def create_chequera(db: Session, chequera: CreateChequera):
    db_chequera = Chequera(**chequera.model_dump())
    db.add(db_chequera)
    db.commit()
    db.refresh(db_chequera)
    return db_chequera

def get_chequeras(db: Session, limit: int = 100):
    return db.query(Chequera).limit(limit).all()
