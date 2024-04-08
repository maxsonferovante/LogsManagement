from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ConnectionHandler:
    def __init__(self):
        self.__connection_string = "{}:///{}".format(
            "sqlite",
            "storage.db")

        self.__engine = None
        self.session = None

    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string)

    def _get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self._get_engine())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


db_connection_handler = ConnectionHandler()
