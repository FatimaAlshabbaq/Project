from fastapi import APIRouter, HTTPException
from app.schemas import ItemCreate, Item
from app import crud

router = APIRouter()

@router.post("", response_model=Item, status_code=201)
async def create_item_endpoint(payload: ItemCreate):
    """Create an item."""
    return crud.create_item(payload)

@router.get("/{item_id}", response_model=Item)
async def get_item_endpoint(item_id: int):
    item = crud.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    return item

@router.get("", response_model=list[Item])
async def list_items_endpoint():
    return crud.list_items()