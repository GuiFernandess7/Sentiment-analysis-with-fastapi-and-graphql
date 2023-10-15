from fastapi import FastAPI
from .schemas import graphql_app

from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='FastAPI MySQL Docker',
        description='Test Run FastAPI and MySQL in Docker',
        version='1.0'
)
app.include_router(graphql_app, prefix='/app')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)