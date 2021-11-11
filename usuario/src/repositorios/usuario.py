from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario
from src.models import models

class RepositorioUsuario():

    def __init__(self, db: Session):
        self.db = db
    
    def criar(self, usuario: Usuario):
        db_usuario = models.Usuario(nome=usuario.nome,
                                    email=usuario.email,
                                    senha=usuario.senha,
                                    github=usuario.github)

        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario

    def listar(self):
        usuarios = self.db.query(models.Usuario).all()
        return usuarios

    def obter_usuario(self, usuario_id: int):
        usuario = self.db.query(models.Produto).filter_by(id=usuario_id).one()
        return usuario

    def remover_usuario(self, usuario_id: int):
        usuario = self.db.delete(models.Usuario).where(models.Usuario.id == usuario_id)
        self.db.commit()
        return usuario
