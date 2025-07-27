import logging
from sqlmodel import SQLModel, create_engine
from settings import settings

sqlite_url = f"sqlite:///{settings.sqlite_file}"
logging.info(f"Using SQLite database at: {sqlite_url}")
engine = create_engine(sqlite_url, echo=True)