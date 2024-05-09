import decimal

from pydantic import BaseModel


class Tickers(BaseModel):
    ticker: str
    price_avg: decimal.Decimal

class Binance(BaseModel):
    tickers: list[Tickers]

class BinanceStock(BaseModel):
    tickers: list[Tickers]


class GateIoStock(BaseModel):
    tickers: list[Tickers]


class BitGetStock(BaseModel):
    tickers: list[Tickers]


class ByBitStock(BaseModel):
    tickers: list[Tickers]


class BingXStock(BaseModel):
    tickers: list[Tickers]


class BitFinexStock(BaseModel):
    tickers: list[Tickers]


class BitForexStock(BaseModel):
    tickers: list[Tickers]


p = [
    {
        'ticker': 'btc',
        'price_avg': decimal.Decimal(23.7)
    },
    {
        'ticker': 'etf',
        'price_avg': decimal.Decimal(3.7)
    }
]
test = {
    'tickers': p
}
asd = Binance(**test)

print(asd)