from fastapi import HTTPException
import app.schemas.schemaCheque as schema
import app.crud.crudChequera as crudChequera
import app.models.modelChequera as modelChequera



def validate_create_cheque(db ,cheque: schema.BaseCheque):
    chequera = db.query(modelChequera.Chequera).filter(modelChequera.Chequera.id == cheque.chequera_id).first()
    if chequera is None:
        raise HTTPException(status_code=404, detail="Chequera not found")
    
    cheque_db = db.query(modelChequera.Cheque).filter(modelChequera.Cheque.numero_cheque == cheque.numero_cheque).first()
    if cheque_db is not None:
        raise HTTPException(status_code=400, detail="Cheque number already exists")
    
    elif cheque.numero_cheque < chequera.rango_minimo or cheque.numero_cheque > chequera.rango_maximo:
        raise HTTPException(status_code=400, detail="Cheque number is out of range")
    
    elif crudChequera.check_chequera_completa(chequera):
        raise HTTPException(status_code=400, detail="Chequera is complete")