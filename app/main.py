from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, crud
from app.database import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"Aulas de Python"}

@app.get("/usuarios/")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users