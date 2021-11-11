from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from src.config.database import Base


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    github = Column(String)
