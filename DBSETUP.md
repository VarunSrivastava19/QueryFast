# Configuring SQLite with FastAPI using SQLModel

1. **Install Dependencies**
    ```bash
    pip install fastapi[all] uvicorn sqlmodel
    ```

2. **Create a SQLModel Model**
    ```python
    from typing import Optional
    from sqlmodel import SQLModel, Field
    
    class Item(SQLModel, table=True):
         id: Optional[int] = Field(default=None, primary_key=True)
         name: str
         description: Optional[str] = None
    ```

3. **Set Up the Database Engine**
    ```python
    from sqlmodel import create_engine

    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    engine = create_engine(sqlite_url, echo=True)
    ```

4. **Create Database Tables**
    ```python
    SQLModel.metadata.create_all(engine)
    ```

5. **Integrate with FastAPI**
    ```python
    from fastapi import FastAPI

    app = FastAPI()
    ```

6. **Create Dependency for Database Session**
    ```python
    from sqlmodel import Session

    def get_session():
         with Session(engine) as session:
              yield session
    ```

7. **Use the Session in Endpoints**
    ```python
    from fastapi import Depends

    @app.post("/items/")
    def create_item(item: Item, session: Session = Depends(get_session)):
         session.add(item)
         session.commit()
         session.refresh(item)
         return item
    ```

8. **Run the Application**
    ```bash
    uvicorn main:app --reload
    ```
# Project Scaffolding: Keep the following things in mind:
# Project Scaffolding? Keep following thing in mind:

1. **Ordered Imports**
    ```python
    # main.py - FastAPI entrypoint file
    
    # Import the models first to ensure they are registered with SQLModel's metadata
    # before calling create_all; otherwise, tables may not be created.
    from db.models.item import Item
    from db.index import engine # Now import the engine
    SQLModel.metadata.create_all(engine) # Then associate with db
    ```