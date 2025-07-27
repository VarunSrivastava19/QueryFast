from fastapi import FastAPI
import logging
from sqlmodel import SQLModel
from routes.root import router as root_router
from routes.about import router as about_router
from routes.messages import router as messages_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from fastapi.middleware.cors import CORSMiddleware
from settings import settings

allow_origins = ["http://localhost:4000", "http://127.0.0.1:4000", settings.client_url]


app = FastAPI(
    title="QueryFast",
    description="FastAPI App to query heroes.",
    version="1.0.0",
    contact={"name": "Cheese", "email": "cheese@example.com"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,  # List of allowed origins
    allow_credentials=True,  # Allow credentials (cookies, authorization headers, etc.)
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],  # Allow all HTTP headers
)

"""
Look at the following 2 import lines
"""
from db.models.hero import Hero
from db.index import engine
"""
They are called in this specific order to ensure that the Hero model is registered with SQLModel
before the engine is created. This is important for SQLModel to recognize the model when creating the
database schema.

If the order is changed, the Hero model, or any other model, will not be recognized by SQLModel, and
won't be included in the database schema when the engine is created.

So, first import all the db models, then import the db engine to initialize the database with the models.

This is a quite stark way to do it, unlike in Express where you just dynamically import models, just place em in 
a folder and run a for loop to import them all into the Sequelize database singleton.
"""
SQLModel.metadata.create_all(engine)

app.include_router(root_router)
app.include_router(about_router)
app.include_router(messages_router)
