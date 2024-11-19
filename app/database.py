from sqlalchemy import create_engine
from sqlalchemy import Sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time

#Começando a conexão com banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:/// ./banco.db"

#Criando variáveis para a interação com o banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = Sessionmaker(autocommit=False, autoflus=False, bind=engine)

Base = declarative_base