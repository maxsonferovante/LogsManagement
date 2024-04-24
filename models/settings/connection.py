from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import insert, delete, select, update

from models.settings.base import Base

class ConnectionHandler:
    def __init__(self):
        self.__connection_string = "{}:///{}".format(
            "sqlite",
            "storage.db")

        self.__engine = None
        self.session = None

    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string,
                                      future=True,)
        Base.metadata.create_all(self.__engine)  
        
    def _get_engine(self):
        return self.__engine

    def __enter__(self):
        self.session = Session(bind=self._get_engine(),
                               future=True,
                               autoflush=False,
                               expire_on_commit=False)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


db_connection_handler = ConnectionHandler()
