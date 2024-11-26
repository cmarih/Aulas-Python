from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time

#Começando a conexão com banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:/// ./banco.db"

#Criando variáveis para a interação com o banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflus=False, bind=engine)

Base = declarative_base

connected = False
while not connected:
    try:
        engine = engine = create_engine(SQLALCHEMY_DATABASE_URL)
        connected = True
    except Exception as e:
        print(f"Erro ao tentar se conectar: {e}")
        time.sleep(5)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()