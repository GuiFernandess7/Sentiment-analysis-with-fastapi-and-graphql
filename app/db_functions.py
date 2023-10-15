from .models import HistoryData
from .database import engine, get_session
from .processing import clean_sentence, analyze_sentence 
from sqlmodel import Session, select
import datetime

session = get_session()

def get_data():
    query = select(HistoryData)
    with Session(engine) as session:
        result = session.execute(query).scalars().all()
    return result

def add_data(sentence: str):
    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    cleaned_sentence = clean_sentence(sentence)
    sentiment_data = analyze_sentence(cleaned_sentence)
    history_data = HistoryData(
        created_at=timestamp,
        sentences=sentence,
        clean_sentences=cleaned_sentence,
        sentiment=sentiment_data['sentiment'],
        sentiment_score=sentiment_data['sentiment_score']
    )
    with Session(engine) as session:
        session.add(history_data)
        session.commit()
        session.refresh(history_data) 
    
    return history_data