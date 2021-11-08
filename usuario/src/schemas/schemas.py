from pydantic import BaseModel
from typing import Optional, List

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_model = True