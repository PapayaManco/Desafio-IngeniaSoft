import pydantic as pydantic

class BaseChequera(pydantic.BaseModel):
    nombre_banco: str
    rango_minimo: int
    rango_maximo: int

class Chequera(BaseChequera):
    id: int

    class Config:
        from_attributes = True


class CreateChequera(BaseChequera):
    pass

