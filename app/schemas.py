import strawberry
from strawberry.fastapi import GraphQLRouter
import datetime
from .db_functions import get_data, add_data

@strawberry.type
class HistoryDataSchema:
    id: int
    created_at: datetime.datetime
    sentences: str
    clean_sentences: str
    sentiment: str
    sentiment_score: float

@strawberry.type
class Query:
    get_data: list[HistoryDataSchema] = strawberry.field(resolver=get_data)

@strawberry.type
class Mutation:
    add_data: HistoryDataSchema = strawberry.field(resolver=add_data)

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation)

graphql_app = GraphQLRouter(schema)