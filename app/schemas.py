from typing import Optional
import strawberry
from strawberry.fastapi import GraphQLRouter
import datetime
from .db_functions import get_data

@strawberry.type
class SentimentSchema:
    id: int
    created_at: datetime.datetime
    sentences: str
    clean_sentences: str
    sentiment: str
    sentiment_score: float

@strawberry.type
class Query:
    get_data: list[SentimentSchema] = strawberry.field(resolver=get_data)

schema = strawberry.Schema(
    query=Query)

graphql_app = GraphQLRouter(schema)