from json import load
import os.path
from Models.ConfigModels import ConfigDB

class Base:

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

class CreateEngine(Base):

    def getEngine(
            self,

    ):
        pass

    def _getConnStr(
            self,
    ) -> str:
        return (f'{self._config.dialect}+'
                f'{self._config.driver}://'
                f'{self._config.username}:'
                f'{self._config.password}@'
                f'{self._config.host}:'
                f'{self._config.port}/'
                f'{self._config.database}')


asdaf = CreateEngine()
print(asdaf._getConnStr())







