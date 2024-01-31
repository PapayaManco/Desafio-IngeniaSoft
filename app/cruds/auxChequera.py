from fastapi import HTTPException

def validate_create_chequera(chequera):
    if chequera.rango_maximo < 0 or chequera.rango_minimo < 0:
        raise HTTPException(status_code=400, detail="Rango maximo y minimo tienen que positivos")
    elif chequera.rango_minimo >= chequera.rango_maximo:
        raise HTTPException(status_code=400, detail="Rango maximo tiene que ser mayor que rango minimo")
    elif (get_range_total(chequera)) > 30:
        raise HTTPException(status_code=400, detail="La diferencia entre el rango maximo y minimo no puede ser mayor a 30 valores")

def get_range_total(chequera):
    return (chequera.rango_maximo - chequera.rango_minimo + 1)

def check_chequera_completa(chequera):
    return len(chequera.cheques) == get_range_total(chequera)

def check_chequera_exists(chequera):
     if chequera is None:
        raise HTTPException(status_code=404, detail="Chequera no encontrada")