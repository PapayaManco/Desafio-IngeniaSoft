from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.modelCheque import Cheque
 
class Chequera(Base):
    __tablename__ = "chequeras"
    id = Column(Integer, primary_key=True, index=True)
    nombre_banco = Column(String, index=True)
    rango_minimo = Column(Integer)
    rango_maximo = Column(Integer)
    cheques = relationship("Cheque", back_populates="chequera")