from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TIPO_BANCO = 'sqlite'
NOME = 'storage.db'

class __DBConnetionHandler:
    def __init__(self) -> None:
        self.__connection_engine = f'{TIPO_BANCO}:///{NOME}'
        self.__engine = None
        self.session = None

    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_engine)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

db_connection_handler = __DBConnetionHandler()