from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from APIs.config.db import SessionLocal
from APIs.models.user import products
import uvicorn

app = FastAPI()
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# Dependencia para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/Products")
def get_customers(db: Session = Depends(get_db)):
    
    products_API = db.query(products).filter(products.supplier_ids == 1).all()

    return products_API