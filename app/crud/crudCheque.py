from sqlalchemy.orm import Session
import app.models.modelCheque as model
import app.schemas.schemaCheque as schema

async def create_cheque(
        db: Session, 
        cheque: schema.BaseCheque ) -> schema.Cheque:
    cheque = model.Cheque(**cheque.model_dump())
    db.add(cheque)
    db.commit()
    db.refresh(cheque)
    return schema.Cheque.model_validate(cheque)



