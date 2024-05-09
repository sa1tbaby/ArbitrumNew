from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.engine.base import Engine
from os.path import abspath as path_abspath
from Models.ConfigModels import ConfigDB
import logging

from json import load
import os.path


class BaseDB:

    def __init__(
            self
    ):
        self._config = self.getConfig()

    def getConfig(
            self,
            config_path: str = 'Configs',
            config_name: str = 'ConfigDB.json'
    ):
        cur_dir = os.path.abspath(os.path.curdir)
        config_path = os.path.join(cur_dir, config_path, config_name)

        with open(config_path, 'r') as file:
            self._config = ConfigDB(**load(file))

        return self._config


class CreateEngine(BaseDB):

    def getEngine(self) -> Engine:
        return create_engine(
            url=self._getConnStr(),
            echo=self._config.engine_echo,
            pool_size=self._config.engine_pool_size
        )

    def _getConnStr(self) -> str:
        return (f'{self._config.dialect}+'
                f'{self._config.driver}://'
                f'{self._config.username}:'
                f'{self._config.password}@'
                f'{self._config.host}:'
                f'{self._config.port}/'
                f'{self._config.database}')






class AlchManager:

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

