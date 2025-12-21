# Python Tutorials

This folder contains working code examples for each tutorial on the Chicas Code website.

## Prerequisites

- Python 3.10+ (should already be installed)
- `uv` package manager (should already be installed)
- VS Code

## Tutorials

### 1. Hello Python
Basic Python setup with virtual environments and your first program.
📁 `hello-python/`

### 2. APIs with FastAPI
Build a web API that greets you by name.
📁 `fastapi-hello/`

### 3. Store API + Database
Add a local NoSQL database and build a product store API.
📁 `store-api/`

### 4. Storefront UI
Create a simple web interface for your store (uses the store-api).
📁 `store-api/index.html`

## Quick Start

Each tutorial folder has its own README with specific instructions. General pattern:

```bash
cd <tutorial-folder>
uv venv
uv pip install <dependencies>
uv run python <script>.py  # or uvicorn for APIs
```

## Tips

- Each project gets its own virtual environment (`.venv/`)
- Database files (`*.json`) are gitignored
- Use `uv run` to execute commands in the project's venv
- For APIs, visit `/docs` endpoint for interactive documentation
