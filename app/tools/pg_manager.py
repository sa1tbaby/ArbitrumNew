from sqlalchemy import create_engine as alch_create_engine
from sqlalchemy.orm import Session, sessionmaker
from os.path import abspath as path_abspath
import logging


class AlchManager(object):
    """


    """
    alch_dialect = 'postgresql'
    alch_driver = 'psycopg2'
    alch_username = 'cesium'
    alch_host = '192.168.1.148'
    alch_port = '5432'

    def __init__(self,
                 alch_database: str,
                 alch_password: str = 'user',
                 logging_file: str = 'AlchManager_log.txt',
                 logging_level=logging.DEBUG,
                 engine_echo=True,
                 engine_pool_size=5):

        self.__alch_password = alch_password
        self.alch_database = alch_database

        self.logging_create(
            logging_file=logging_file,
            logging_level=logging_level,
            logging_file_mode='w',
            logging_format=f"AlchManager.%(funcName)s : %(asctime)s : %(levelname)s\n%(message)s")

        self.logger_engine = logging.getLogger('AlchManager_engine')
        self.logger_session = logging.getLogger('AlchManager_session')

        session = sessionmaker(
            bind=self.engine_create(
                engine_create_echo=engine_echo,
                engine_create_pool_size=engine_pool_size)
        )

        self.alch_session = session()

        self.latest_data = None

    def logging_create(self,
                       logging_format,
                       logging_file,
                       logging_level,
                       logging_file_mode):

        logging.basicConfig(
            level=logging_level,
            filename=path_abspath(logging_file),
            filemode=logging_file_mode,
            format=logging_format)

    def engine_create(self,
                      engine_create_echo,
                      engine_create_pool_size):
        try:
            engine_connect_string = f'{self.alch_dialect}+' \
                             f'{self.alch_driver}://' \
                             f'{self.alch_username}:' \
                             f'{self.__alch_password}@' \
                             f'{self.alch_host}:' \
                             f'{self.alch_port}/' \
                             f'{self.alch_database}'

            engine = alch_create_engine(url=engine_connect_string,
                                        echo=engine_create_echo,
                                        pool_size=engine_create_pool_size)
        except Exception as exc:
            print(exc)
            self.logger_engine.critical('engine_create was failed\n',
                                        exc)

        else:
            self.logger_engine.info('operation was successfully finished\n'
                                    f'{engine.engine}\n')

            return engine

    def session_add(self,
                    data: list,
                    session: Session,
                    ):
        try:
            session.add_all(data)

            self.latest_data = session.new

            session.commit()

        except Exception as exc:
            print(exc)
            self.logger_session.critical(f'AlchManager_session_add commit data to {session.info} was failed\n',
                                         exc)
        else:
            self.logger_engine.info(f'AlchManager_session_add commit success {session.info}\n')
            self.logger_engine.debug(f'AlchManager_session_add commit success {session.info}\n'
                                         f'and data was: \n{self.latest_data}')
            return True

    def session_get(self,
                    value: int,
                    table):
        print(self.alch_session.query(table).all())
        return self.alch_session.query(table).all()

    @property
    def latest_adding_data(self):
        return self.latest_data

