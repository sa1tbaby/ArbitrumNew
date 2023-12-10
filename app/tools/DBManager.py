from sqlalchemy import create_engine as alch_create_engine
from sqlalchemy.orm import Session, sessionmaker
from os.path import abspath as path_abspath
from Models.ConfigModels import ConfigDB
import logging


class AlchManager:
    """


    """

    def __init__(
            self,
            config: ConfigDB
    ):

        self._config = config
        self._logger = logging.getLogger('AlchManager')

    def engine_create(self,
                      engine_create_echo,
                      engine_create_pool_size):
        try:
            engine_connect_string = f'{self._config.dialect}+' \
                             f'{self._config.driver}://' \
                             f'{self._config.username}:' \
                             f'{self.__alch_password}@' \
                             f'{self._config.host}:' \
                             f'{self._config.port}/' \
                             f'{self._config.database}'

            engine = alch_create_engine(url=engine_connect_string,
                                        echo=engine_create_echo,
                                        pool_size=engine_create_pool_size)
        except Exception as exc:
            print(exc)
            self._logger.critical('engine_create was failed\n',
                                        exc)

        else:
            self._logger.info('operation was successfully finished\n'
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
            self._logger.critical(f'AlchManager_session_add commit data to {session.info} was failed\n',
                                         exc)
        else:
            self._logger.info(f'AlchManager_session_add commit success {session.info}\n')
            self._logger.debug(f'AlchManager_session_add commit success {session.info}\n'
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

