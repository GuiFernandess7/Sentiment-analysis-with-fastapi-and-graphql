from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from .schemas import graphql_app

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def welcome():
    return JSONResponse({"message": "Welcome!"})

app.include_router(graphql_app, prefix='/graphql')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)