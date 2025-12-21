# Tutorial 3 & 4: Store API + Storefront UI

A FastAPI application with a local NoSQL database (TinyDB) and a simple HTML storefront.

## Setup

```bash
# Create virtual environment
uv venv

# Install dependencies
uv pip install fastapi uvicorn tinydb
```

## Run the API

```bash
uv run uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000

## Add Sample Products

Visit http://127.0.0.1:8000/docs and use the interactive API to add products:

1. Click on `POST /products`
2. Click "Try it out"
3. Add a product (example):
```json
{
  "name": "Laptop",
  "price": 999.99
}
```
4. Click "Execute"

Add a few more products:
- `{"name": "Mouse", "price": 29.99}`
- `{"name": "Keyboard", "price": 79.99}`
- `{"name": "Monitor", "price": 299.99}`

## View the Storefront

Open `index.html` in your browser to see the store UI. You can:
- Search for products
- Click "Buy Now" to simulate a purchase
- All data persists in `store.json`

## API Endpoints

- `GET /` - Welcome message
- `GET /products` - List all products
- `POST /products` - Add a new product
- `GET /products/{id}` - Get a specific product
