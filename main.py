from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import engine
from database import SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "api is running"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()