from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ItemUpdate(ItemCreate):
    name: str

    class Config:
        orm_mode = True
