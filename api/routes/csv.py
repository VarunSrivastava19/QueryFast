from fastapi import APIRouter

router = APIRouter()

@router.get("/csv")
async def about() -> dict[str, str]:
    return {"message": "I am CSV microservice in native app service!"}