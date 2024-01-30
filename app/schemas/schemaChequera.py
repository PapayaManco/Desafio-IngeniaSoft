import pydantic as pydantic
from pydantic import validator

class BaseChequera(pydantic.BaseModel):
    nombre_banco: str
    rango_minimo: int
    rango_maximo: int

    @validator("rango_minimo")
    def validate_rango_minimo(cls, value, values):
        if "rango_maximo" in values and value >= values["rango_maximo"]:
            raise ValueError("rango_minimo must be smaller than rango_maximo")
        return value

class Chequera(BaseChequera):
    id: int

    class Config:
        from_attributes = True


class CreateChequera(BaseChequera):
    pass

