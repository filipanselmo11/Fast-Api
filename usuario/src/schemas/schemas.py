from pydantic import BaseModel
from typing import Optional, List

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    senha: str
    github: str

    class Config:
        orm_model = True