# import logging
from dataclasses import dataclass
import os
import time
import sqlalchemy
import sqlalchemy.exc


@dataclass
class Config:
    host: str
    username: str
    password: str
    database: str
    port: int

    @property
    def url(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"


config = Config(
    host=os.getenv("POSTGRES_HOST", "localhost"),
    username=os.getenv("POSTGRES_USERNAME", "postgres"),
    password=os.getenv("POSTGRES_PASSWORD", "postgres"),
    port=int(os.getenv("POSTGRES_PORT", 5432)),
    database=os.getenv("POSTGRES_DB", "postgres"),
)

engine = sqlalchemy.create_engine(url=config.url)


# Database is not getting started before the application
# Workaround: implement reconnect mechanism
try:
    engine.connect()
except sqlalchemy.exc.OperationalError as e:
    print("Connection failed; Retrying in few seconds...")
    time.sleep(10)
    try:
        engine.connect()
        print("Connection successful!")
    except Exception as e:
        print(e)

