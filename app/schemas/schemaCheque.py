import pydantic as pydantic

class BaseCheque(pydantic.BaseModel):
    numero_cheque: int
    chequera_id: int

class Cheque(BaseCheque):
    id: int

    class Config:
        from_attributes = True

class CreateCheque(BaseCheque):
    pass
