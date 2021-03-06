from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    #produtos: List[produtos] = []

    class Config:
        orm_mode = True


class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = None
