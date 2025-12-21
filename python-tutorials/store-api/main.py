from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from tinydb import TinyDB, Query
from pydantic import BaseModel

app = FastAPI()

# Add CORS middleware to allow browser requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db = TinyDB("store.json")
products_table = db.table("products")

class Product(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Store API"}

@app.get("/products")
def get_products():
    return products_table.all()

@app.post("/products")
def add_product(product: Product):
    product_id = products_table.insert(product.dict())
    return {"id": product_id, **product.dict()}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = products_table.get(doc_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"id": product_id, **product}
