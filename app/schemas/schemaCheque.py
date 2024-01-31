import pydantic as pydantic

class BaseCheque(pydantic.BaseModel):
    chequera_id: int
    numero_cheque: int
    

class Cheque(BaseCheque):
    id: int

    class Config:
        from_attributes = True
