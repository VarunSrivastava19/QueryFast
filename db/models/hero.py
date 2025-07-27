from datetime import date
from typing import Optional
from sqlmodel import Field, SQLModel


class HeroBase(SQLModel):
    name: str
    username: str = Field(index=True, unique=True)
    secret_name: str
    date_of_birth: Optional[date] = None


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CreateHero(HeroBase):
    pass
