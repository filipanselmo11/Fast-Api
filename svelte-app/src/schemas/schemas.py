from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    senha: str
    github: str

    class Config:
        orm_mode = True

class Tecnologia(BaseModel): 
    id: Optional[int] = None
    nome: str

    class Config:
        orm_mode = True