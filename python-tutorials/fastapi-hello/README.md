# Tutorial 2: FastAPI Hello

A simple FastAPI application that greets you by name.

## Setup

```bash
# Create virtual environment
uv venv

# Install dependencies
uv pip install fastapi uvicorn
```

## Run

```bash
uv run uvicorn main:app --reload
```

## Try it

- Visit http://127.0.0.1:8000 - see `{"message": "Hello, World!"}`
- Visit http://127.0.0.1:8000/hello/Alice - see `{"message": "Hello, Alice!"}`
- Visit http://127.0.0.1:8000/docs - interactive API documentation
