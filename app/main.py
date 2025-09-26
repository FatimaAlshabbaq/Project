from fastapi import FastAPI
from app.routers import users, items
from app import crud

app = FastAPI(title="Course Project API", version="0.1.0")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])

@app.get("/health", tags=["misc"])
async def health():
    """Simple health check."""
    return {"status": "ok"}