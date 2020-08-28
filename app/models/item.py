from sqlalchemy import Column, Integer, String

from app.core.db import Base


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), comment="测试字段")
