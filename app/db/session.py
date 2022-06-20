from sqalchemy import create_engine
from sqalchemy.orm import sessionmaker

SQALCHEMY_DATABASE_URI = "sqlite:///example.db"

engine = create_engine(
    SQALCHEMY_DATABASE_URI,
    connect_args = {"check_same_thread" : False},
)

SessionLocal = sessionmaker(autocommit = False, autoFlush = False, bind = engine)