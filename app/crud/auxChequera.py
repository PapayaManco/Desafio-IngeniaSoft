from fastapi import HTTPException

def validate_create_chequera(chequera):
    if chequera.rango_maximo < 0 or chequera.rango_minimo < 0:
        raise HTTPException(status_code=400, detail="rango_maximo and rango_minimo must be greater than 0")
    elif chequera.rango_minimo >= chequera.rango_maximo:
        raise HTTPException(status_code=400, detail="rango_minimo must be smaller than rango_maximo")
    elif (get_range_total(chequera)) > 30:
        raise HTTPException(status_code=400, detail="the difference between rango_maximo and rango_minimo must be smaller than 30")

def get_range_total(chequera):
    return (chequera.rango_maximo - chequera.rango_minimo + 1)

def check_chequera_completa(chequera):
    return len(chequera.cheques) == get_range_total(chequera)
