from fastapi import FastAPI
from routes.root import router as root_router
from routes.about import router as about_router
from routes.messages import router as messages_router

from fastapi.middleware.cors import CORSMiddleware
from settings import settings

allow_origins = ["http://localhost:4000", "http://127.0.0.1:4000", settings.client_url]


app = FastAPI(
    title="QueryFast",
    description="A simple FastAPI application to demonstrate message handling",
    version="1.0.0",
    contact={"name": "Cheese", "email": "cheese@example.com"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,  # List of allowed origins
    allow_credentials=True,  # Allow credentials (cookies, authorization headers, etc.)
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)


app.include_router(root_router)
app.include_router(about_router)
app.include_router(messages_router)
