from fastapi import APIRouter

router = APIRouter()

@router.get("/about")
async def about() -> dict[str, str]:
    return {"message": "QueryFast will query heroes!"}