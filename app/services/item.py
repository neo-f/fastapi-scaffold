from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate
from app.services import BaseService


class ItemService(BaseService[Item, ItemCreate, ItemUpdate]):
    pass
