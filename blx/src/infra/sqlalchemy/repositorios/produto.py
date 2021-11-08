from sqlalchemy.orm import Session
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.models import models


class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: Produto):
        db_produto = models.Produto(nome=produto.nome,
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel)
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos

    def obter(self, produto_id: int):
        produto = self.db.query(models.Produto).filter_by(id=produto_id).one()
        return produto

    def remover(self, produto_id: int):
       produto = self.db.delete(models.Produto).where(models.Produto.id == produto_id)
       self.db.commit()
       return produto
