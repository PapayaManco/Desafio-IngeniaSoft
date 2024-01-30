from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Cheque(Base):
    __tablename__ = "cheques"

    id = Column(Integer, primary_key=True, index=True)
    numero_cheque = Column(Integer, index=True)
    chequera_id = Column(Integer, ForeignKey("chequeras.id"))
    chequera = relationship("Chequera", back_populates="cheques")