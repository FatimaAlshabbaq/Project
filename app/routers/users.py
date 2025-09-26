from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, User
from app import crud

router = APIRouter()

@router.post("", response_model=User, status_code=201)
async def create_user_endpoint(payload: UserCreate):
    """Create a new user."""
    return crud.create_user(payload)

@router.get("/{user_id}", response_model=User)
async def get_user_endpoint(user_id: int):
    user = crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user