import pydantic as pydantic
from .schemaCheque import Cheque

class BaseChequera(pydantic.BaseModel):
    nombre_banco: str
    rango_minimo: int
    rango_maximo: int

class Chequera(BaseChequera):
    id: int

    class Config:
        from_attributes = True

class ChequeraWithCheques(BaseChequera):
    id: int
    cheques: list[Cheque]
    
    class Config:
        from_attributes = True

class UpdateChequera(pydantic.BaseModel):
    nombre_banco: str
