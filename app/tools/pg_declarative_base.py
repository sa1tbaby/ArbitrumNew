from sqlalchemy import Column, NUMERIC, VARCHAR
from sqlalchemy.ext.declarative import declarative_base as alch_ext_declarative_base

Base = alch_ext_declarative_base()


class ApiKeys(Base):
    __tablename__ = "api_keys"
    id = Column(NUMERIC, primary_key=True, nullable=False)
    ticker = Column(VARCHAR, nullable=True)
    public = Column(VARCHAR, nullable=True)
    private = Column(VARCHAR, nullable=True)

class Binance(Base):
    __tablename__ = "binance"
    binance_id = Column(NUMERIC, primary_key=True, nullable=False)
