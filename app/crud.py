from sqlalchemy.orm import Session
from . import models

#Buscar usuários
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first

def get_users(db: Session, skip: int = 0, limit:int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

#Criar/inserir usuários
def create_user(db: Session, user: models.User):
    db.add(user)
    db.commit() #Confirmar/salvar as alterações realizadas
    db.refresh(user) #atualiza as informações no banco de dados
    return

#Update de Usuários
def update_user(db: Session, user_id: int, nome: str, email: str, idade: int):
    user = get_user(db, user_id) #Buscar o ID no banco de dados
    if user:
        user.nome = nome
        user.email = email
        user.idade = idade
        db.commit() #Confirmar/salvar as alterações realizadas
        db.refresh(user) #atualiza as informações no banco de dados
        return user
    return None

#Deletando Usuários
def dele_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user) #Confirmar/salvar as alterações realizadas
        db.commit() #atualiza as informações no banco de dados
        return True
    return False