from binance import Client as bin_Client
from app.tools import pg_manager
from app.tools.pg_declarative_base import ApiKeys


class BinanceManager(pg_manager.AlchManager):


    def __init__(self,
                 alch_database: str):

        super().__init__(alch_database=alch_database)

        tresh = self.session_get(table=ApiKeys,
                                 value=1)

        print(tresh)
        #self.client = bin_Client('api_key', 'api_secret')


tst = BinanceManager(alch_database='arbitrum_db_1')
