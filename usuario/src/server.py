from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm.session import Session
from src.config.database import get_db
from src.schemas.schemas import Usuario
from src.repositorios.usuario import RepositorioUsuario



app = FastAPI()


@app.get("/")
async def root():
    return {"mensagem": "Olá Mundo"}



#Usuarios

@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado


@app.get('/usuarios', status_code=status.HTTP_200_OK, response_model=List[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios
