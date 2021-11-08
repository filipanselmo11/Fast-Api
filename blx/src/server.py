from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm.session import Session
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.schemas.schemas import Produto, Usuario
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario

#criar_db()

app = FastAPI()

@app.get('/')
def root():
    return {'messangem': 'API v0.0.1'}

# Produtos

@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=Produto)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.get('/produtos/{produto_id}', status_code=status.HTTP_200_OK, response_model=List[Produto])
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = RepositorioProduto(db).obter(produto_id)
    return produto
    

@app.delete('/produtos/{produto_id}')
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = RepositorioProduto(db).remover(produto_id)
    return produto

# Usuarios
@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario:Usuario, session: Session = Depends(get_db())):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@app.get('/usuarios', status_code=status.HTTP_200_OK, response_model = List[Usuario])
def listar_usuario(session: Session = Depends(get_db())):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios