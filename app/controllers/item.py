from typing import Generic, TypeVar

from fastapi import Depends
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session
from fastapi_utils.cbv import cbv

from app import services, schemas
from app.core.db import get_db
from app.models.item import Item

T = TypeVar("T")


class Controller(Generic[T]):
    model: T
    db: Session

    def retrieve(self, pk) -> T:
        return self.db.query(self.model).get(pk)


router = InferringRouter()


@cbv(router)
class ItemController:
    session: Session = Depends(get_db)

    @router.post("/item")
    def create_item(self, item: schemas.ItemCreate) -> Item:
        return services.item.create(self.session, item)
