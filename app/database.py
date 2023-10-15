"""    
create_engine é usado para criar um mecanismo de banco de dados baseado na URL do banco de dados e outras configurações especificadas.
connect_args={"check_same_thread": False} é um argumento adicional para a conexão SQLite, que permite que várias threads possam acessar 
o banco de dados simultaneamente. Isso é específico para SQLite e geralmente não é necessário para outros SGBDs.

sessionmaker é usado para criar uma fábrica de sessões que gera sessões SQLAlchemy.
autocommit=False: Configuração que desativa o modo de autocommit, o que significa que as transações não serão confirmadas automaticamente. Isso permite que você gerencie as transações manualmente.
autoflush=False: Configuração que desativa o autoflush, o que significa que as alterações não são automaticamente enviadas para o banco de dados. 
Isso também permite um maior controle sobre quando as alterações são realmente enviadas ao banco de dados.
bind=engine: Especifica o mecanismo de banco de dados (engine) a ser usado para a criação de sessões.
declarative_base é uma função de fábrica no SQLAlchemy que produz uma classe base para definições de classes declarativas. 
Essa classe base serve como uma base para criar classes mapeadas (que representam tabelas no banco de dados) no SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
