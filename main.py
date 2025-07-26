from fastapi import FastAPI
from routes.root import router as root_router
from routes.about import router as about_router
from routes.messages import router as messages_router

app = FastAPI(
    title="QueryFast",
    description="A simple FastAPI application to demonstrate message handling",
    version="1.0.0",
    contact={
        "name": "Cheese",
        "email": "cheese@example.com"
    }
)

app.include_router(root_router)
app.include_router(about_router)
app.include_router(messages_router)
