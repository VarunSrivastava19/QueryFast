from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root() -> dict[str, str]:
    return {"message": "QueryFast is up and running!"}