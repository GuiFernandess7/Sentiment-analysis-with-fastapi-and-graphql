from sqlalchemy import Column, Integer, String, TIMESTAMP, FLOAT
from sqlalchemy.orm import relationship

from .database import Base

class SentimentData(Base):
    __tablename__ = "sentiment_data"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(TIMESTAMP, nullable=False)
    sentences = Column(String(300), nullable=False)
    clean_sentences = Column(String(300), nullable=False)
    sentiment = Column(String(8), nullable=False)
    sentiment_score = Column(FLOAT, nullable=False)