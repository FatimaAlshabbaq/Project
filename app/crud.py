from typing import Dict, List, Optional
from .schemas import UserCreate, User, ItemCreate, Item

_users: Dict[int, User] = {}
_items: Dict[int, Item] = {}
_user_id = 1
_item_id = 1

def reset_db() -> None:
    global _users, _items, _user_id, _item_id
    _users = {}
    _items = {}
    _user_id = 1
    _item_id = 1

def create_user(u: UserCreate) -> User:
    global _user_id
    user = User(id=_user_id, **u.dict())
    _users[_user_id] = user
    _user_id += 1
    return user

def get_user(user_id: int) -> Optional[User]:
    return _users.get(user_id)

def create_item(i: ItemCreate) -> Item:
    global _item_id
    item = Item(id=_item_id, **i.dict())
    _items[_item_id] = item
    _item_id += 1
    return item

def get_item(item_id: int) -> Optional[Item]:
    return _items.get(item_id)

def list_items() -> List[Item]:
    return list(_items.values())