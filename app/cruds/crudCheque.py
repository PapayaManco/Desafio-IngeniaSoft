from sqlalchemy.orm import Session
import app.models.modelCheque as model
import app.schemas.schemaCheque as schema

async def create_cheque(db: Session, cheque: schema.BaseCheque ) -> schema.Cheque:
    cheque = model.Cheque(**cheque.model_dump())
    db.add(cheque)
    db.commit()
    db.refresh(cheque)
    return schema.Cheque.model_validate(cheque)

async def get_cheques(db: Session, limit: int) -> list[schema.Cheque]:
    return [schema.Cheque.model_validate(cheque) for cheque in db.query(model.Cheque).limit(limit).all()]


async def update_cheque(db: Session, cheque_id: int, cheque: schema.BaseCheque) -> schema.Cheque:
    cheque_db = db.query(model.Cheque).filter(model.Cheque.id == cheque_id).first()
    for key, value in cheque.model_dump().items():
        setattr(cheque_db, key, value)
    db.commit()
    db.refresh(cheque_db)
    return schema.Cheque.model_validate(cheque_db)

async def delete_cheque(db: Session, cheque_id: int) -> None:
    cheque = db.query(model.Cheque).filter(model.Cheque.id == cheque_id).first()
    db.delete(cheque)
    db.commit()
    return {"message": "Cheque borrado"}
