from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario
from src.models import models

class RepositorioUsuario():

    def __init__(self, session: Session):
        self.session = session
    
    def criar(self, usuario: Usuario):
        db_usuario = models.Usuario(nome=usuario.nome,
                                    email=usuario.email,
                                    senha=usuario.senha,
                                    github=usuario.github)

        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario

    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).all()
        return usuarios