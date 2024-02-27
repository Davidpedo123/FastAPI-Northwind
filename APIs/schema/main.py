from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from APIs.config.db import SessionLocal
from APIs.models.user import products, Orders
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    
origins = [
    "http://localhost:3000", 
    "http://127.0.0.1:8000",
    "null"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/Products")
def get_customers(db: Session = Depends(get_db)):
    
    products_API = db.query(products.product_name, products.standard_cost).filter(products.supplier_ids == 1).order_by(products.standard_cost.asc()).all()

    return products_API
@app.get("/Orders")
def get_Orders(db: Session = Depends(get_db)):
    query = text("SELECT ship_city, ship_state_province, COUNT(*) AS city_count FROM Orders GROUP BY ship_city, ship_state_province;")
    result = db.execute(query)
    Orders_API = result.fetchall()
    return Orders_API