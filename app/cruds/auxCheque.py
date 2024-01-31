from fastapi import HTTPException
import app.schemas.schemaCheque as schema
import app.cruds.crudChequera as crudChequera
import app.models.modelChequera as modelChequera
from app.cruds.auxChequera import check_chequera_exists, check_chequera_completa

    
def validate_create_cheque(db ,cheque: schema.BaseCheque):
    chequera = db.query(modelChequera.Chequera).filter(modelChequera.Chequera.id == cheque.chequera_id).first()
    check_chequera_exists(chequera)
        
    cheque_db = find_cheque_in_chequera(chequera, cheque.numero_cheque)

    if cheque_db is not None:
        raise HTTPException(status_code=400, detail="Numero de cheque ya existe en la chequera")
    
    elif cheque.numero_cheque < chequera.rango_minimo or cheque.numero_cheque > chequera.rango_maximo:
        raise HTTPException(status_code=400, detail="Numero de Cheque esta fuera del rango.")
    
    elif check_chequera_completa(chequera):
        raise HTTPException(status_code=400, detail="Chequera completa, no se pueden agregar mas cheques.")


def find_cheque_in_chequera(chequera, new_cheque_number):
    cheques = chequera.cheques
    for cheque in cheques:
        if cheque.numero_cheque == new_cheque_number:
            return cheque
    return None
