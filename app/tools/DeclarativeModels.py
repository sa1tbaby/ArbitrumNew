from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import DECIMAL, JSON
from decimal import Decimal

class BaseStock(DeclarativeBase):
    ticker: Mapped[str] = mapped_column(primary_key=True)
    price_avg: Mapped[Decimal] = mapped_column(DECIMAL)
    dom_for_sale: Mapped[dict] = mapped_column(JSON)
    dom_for_buy: Mapped[dict] = mapped_column(JSON)


class BinanceStock(BaseStock):
    __tablename__ = "binance_stock"


class GateIoStock(BaseStock):
    __tablename__ = "gateio_stock"


class BitGetStock(BaseStock):
    __tablename__ = "bitget_stock"


class ByBitStock(BaseStock):
    __tablename__ = "bybit_stock"


class BingXStock(BaseStock):
    __tablename__ = "bingx_stock"


class BitFinexStock(BaseStock):
    __tablename__ = "bitfinex_stock"


class BitForexStock(BaseStock):
    __tablename__ = "bitforex_stock"
