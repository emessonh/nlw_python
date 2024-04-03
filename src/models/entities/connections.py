from sqlalchemy import create_engine
TIPO_BANCO = 'sqlite'
NOME = 'storage.db'

class DBConnetionHandler:
    def __init__(self) -> None:
        self.__connection_engine = f'{TIPO_BANCO}:///{NOME}'
        self.__engine = None

    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_engine)

    def get_engine(self):
        return self.__engine