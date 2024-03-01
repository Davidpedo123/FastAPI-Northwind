from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from APIs.config.db import SessionLocal

from APIs.models.user import products, Orders, ProductCreate
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8009, reload=True)
    
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

# ...

# Ruta para crear un nuevo producto
@app.post("/products/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        # Consulta SQL para insertar el nuevo producto
        query = text("""
            INSERT INTO products
            (supplier_ids, product_code, product_name, description, standard_cost,
            list_price, reorder_level, target_level, quantity_per_unit, discontinued,
            minimum_reorder_quantity, category, attachments)
            VALUES
            (:supplier_ids, :product_code, :product_name, :description, :standard_cost,
            :list_price, :reorder_level, :target_level, :quantity_per_unit, :discontinued,
            :minimum_reorder_quantity, :category, :attachments)
        """)

        # Parámetros para la consulta
        params = product.dict()

        # Ejecuta la consulta
        result = db.execute(query, params)
        db.commit()

        # Devuelve el producto creado
        return {"message": "Producto creado exitosamente", "product_id": result.lastrowid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el producto: {str(e)}")

# ...
