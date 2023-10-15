from .models import SentimentData
from .database import engine
from sqlalchemy.orm import joinedload
from sqlmodel import Session, select

def get_data():
    query = select(SentimentData)
    with Session(engine) as session:
        result = session.execute(query).scalars().all()
    return result