from sqlalchemy.orm import Session
import app.models.modelChequera as model
import app.schemas.schemaChequera as schema

from app.cruds.auxChequera import check_chequera_completa , check_chequera_exists

async def create_chequera(db: Session, chequera: schema.BaseChequera ) -> schema.Chequera:
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
    check_chequera_exists(chequera)
    return schema.ChequeraWithCheques.model_validate(chequera)


async def update_chequera(db: Session, chequera_id: int, chequera: schema.UpdateChequera) -> schema.Chequera:
    chequera_db = db.query(model.Chequera).filter(model.Chequera.id == chequera_id).first()
    check_chequera_exists(chequera_db)
    for key, value in chequera.model_dump().items():
        setattr(chequera_db, key, value)
    db.commit()
    db.refresh(chequera_db)
    return schema.ChequeraWithCheques.model_validate(chequera_db)


async def delete_chequera(db: Session, chequera_id: int):
    chequera = db.query(model.Chequera).filter(model.Chequera.id == chequera_id).first()
    check_chequera_exists(chequera)
    db.query(model.Cheque).filter(model.Cheque.chequera_id == chequera_id).delete()
    db.delete(chequera)
    db.commit()
    return {"message": "Chequera borrada"}