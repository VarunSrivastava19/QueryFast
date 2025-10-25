import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from db.models.hero import CreateHero, Hero, HeroBase
from db.index import engine

logger = logging.getLogger(__name__)

router = APIRouter()


# Session dependency
def get_session():
    with Session(engine) as session:
        yield session


@router.get("/hero/{hero_uname}", response_model=Hero)
async def get_hero(hero_uname: str, session: Session = Depends(get_session)):
    """Get a hero by username."""
    hero = session.exec(select(Hero).where(Hero.username == hero_uname)).first()
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@router.get("/heroes", response_model=list[Hero])
async def get_heroes(
    skip: int = 0, limit: int = 10, session: Session = Depends(get_session)
):
    """Get a list of heroes with pagination."""
    if skip < 0 or limit <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid pagination parameters",
        )
    heroes = session.exec(select(Hero).offset(skip).limit(limit)).all()
    return heroes


@router.post("/heroes", response_model=Hero, status_code=status.HTTP_201_CREATED)
async def create_hero(hero: CreateHero, session: Session = Depends(get_session)):
    """Create a new hero."""
    if not hero.username or not hero.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username and name are required",
        )
    if session.exec(select(Hero).where(Hero.username == hero.username)).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Hero with this username already exists",
        )
    print(f"date of birth type: {type(hero.date_of_birth)}")
    db_hero = Hero(**hero.model_dump())
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


@router.put("/heroes/{hero_id}", response_model=Hero)
async def update_hero(
    hero_id: int, hero: CreateHero, session: Session = Depends(get_session)
):
    """Update an existing hero."""
    if not hero.username or not hero.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username and name are required",
        )
    existing_hero = session.get(Hero, hero_id)
    if not existing_hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    for field, value in hero.model_dump().items():
        setattr(existing_hero, field, value)

    session.commit()
    session.refresh(existing_hero)
    return existing_hero


@router.delete(
    "/heroes/{hero_id}", status_code=status.HTTP_204_NO_CONTENT
)
async def remove_hero(hero_id: int, session: Session = Depends(get_session)):
    """Delete a hero by ID."""
    if hero_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid hero ID",
        )
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    session.delete(hero)
    session.commit()
    return
