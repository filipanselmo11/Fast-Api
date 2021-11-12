from sqlalchemy import Column, Integer, String
from src.config.database import Base


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    github = Column(String)


class Tecnologia(Base):
    __tablename__ = 'tecnologia'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
