import asyncio
from dataclasses import dataclass
from typing import Optional, List, Union
from methods import *
from logs import *
from aiohttp import ClientSession
from REST.decorators import get
from REST.async_base import AsyncClient
from enums import *


class RealClient(AsyncClient):
    def __init__(self):
        super().__init__(BaseURL.BASE, ClientSession())

    @get(PingURL.PING)
    async def ping(self) -> dict:
        """
        Check API server status
        """

    @get(SimpleURL.PRICE)
    async def get_price(self, ids: str, vs_currencies: str = 'usd',
                        include_market_cap: bool = False, include_24hr_vol: bool = False,
                        include_24hr_change: bool = False, include_last_updated_at: bool = False) -> dict:

        """
        Get the current price of any cryptocurrencies in any other supported currencies that you need.
        """

    @get(SimpleURL.TOKEN_PRICE)
    async def get_token_price(self, contract_addresses: str, id: str = 'ethereum', vs_currencies: str = 'usd',
                              include_market_cap: bool = False, include_24hr_vol: bool = False,
                              include_24hr_change: bool = False, include_last_updated_at: bool = False) -> dict:

        """
        Get current price of tokens (using contract addresses)
        for a given platform in any other currency that you need.
        """

    @get(SimpleURL.SUPPORTED_VS_CURRENCIES)
    async def get_supported_vs_currencies(self) -> dict:

        """
        Get list of supported_vs_currencies.
        """

    @get(Coins.LIST)
    async def get_coins_list(self, include_platform: bool = True) -> dict:

        """
        List all supported coins id, name and symbol (no pagination required)
        Use this to obtain all the coins’ id in order to make API calls
        """

    @get(Coins.MARKETS)
    async def get_coins_markets(self, ids: str, vs_currency: str = 'usd', category: str = '',
                                order: Union[MarketSortOrder, str] = MarketSortOrder.MARKET_CAP_DESC,
                                per_page: int = 100, page: int = 1, sparkline: bool = False,
                                price_change_percentage: str = '1h,24h,7d') -> list:

        """
        List all supported coins price, market cap, volume, and market related data
        Use this to obtain all the coins market data (price, market cap, volume)
        """

    @get(Coins.COIN_DATA)
    async def get_coin_by_id(self,
                             id: str,
                             localization: bool = True,
                             tickers: bool = True,
                             market_data: bool = True,
                             community_data: bool = True,
                             developer_data: bool = True,
                             sparkline: bool = False) -> dict:
        """
        Get current data (name, price, market, … including exchange tickers) for a coin.
        IMPORTANT:
        Ticker object is limited to 100 items, to get more tickers, use /coins/{id}/tickers
        Ticker is_stale is true when ticker that has not been updated/unchanged from the exchange for a while.
        Ticker is_anomaly is true if ticker’s price is outliered by our system.
        You are responsible for managing how you want to display these information (e.g. footnote, different background, change opacity, hide)
        """

    @get(Coins.COIN_TICKERS)
    async def get_coin_ticker_by_id(self,
                                    id: str,
                                    exchange_ids: str = '',
                                    include_exchange_logo: bool = False,
                                    page: int = 1,
                                    order: Union[SortOrder, str] = SortOrder.TRUST_SCORE_DESC,
                                    depth: bool = True) -> dict:
        """
        Get coin tickers (paginated to 100 items)
        IMPORTANT:
        Ticker is_stale is true when ticker that has not been updated/unchanged from the exchange for a while.
        Ticker is_anomaly is true if ticker’s price is outliered by our system.
        You are responsible for managing how you want to display these information (e.g. footnote, different background, change opacity, hide)
        """

    @get(Coins.HISTORICAL_DATA)
    async def get_coin_history_by_id(self,
                                     id: str,
                                     date: str,
                                     localization: str = 'en') -> dict:
        """
        Get historical data (name, price, market, stats) at a given date for a coin
        """

    @get(Coins.MARKET_CHART)
    async def get_coin_market_chart_by_id(self,
                                          id: str, vs_currency: str = 'usd', days: str = '7',
                                          interval: Union[Interval, str] = Interval.DAILY) -> dict:
        """
        Get historical market data include price, market cap, and 24h volume (granularity auto)
        Minutely data will be used for duration within 1 day, Hourly data will be used for duration between 1 day and 90 days,
        Daily data will be used for duration above 90 days.

        :param id: pass the coin id (can be obtained from /coins) eg. bitcoin
        :param vs_currency: The target currency of market data (usd, eur, jpy, etc.)
        :param days: Data up to number of days ago (eg. 1,14,30,max)
        :param interval: Data interval. Possible value: daily
        """

    @get(Coins.MARKET_CHART_RANGE)
    async def get_coin_market_chart_range_by_id(self, id: str, from_timestamp: int,
                                                to_timestamp: int, vs_currency: str = 'usd') -> dict:
        """
        Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)
        Minutely data will be used for duration within 1 day, Hourly data will be used for duration between 1 day and
        90 days, Daily data will be used for duration above 90 days.

        :param from_timestamp: From date in UNIX Timestamp (eg. 1392577232)
        :param to_timestamp: To date in UNIX Timestamp (eg. 1422577232)
        :param id: pass the coin id (can be obtained from /coins) eg. bitcoin
        :param vs_currency: The target currency of market data (usd, eur, jpy, etc.)

        """

async def main():
    client = RealClient()
    resp = await client.get_coin_market_chart_range_by_id(id='bitcoin', from_timestamp=1392577232, to_timestamp=1422577232)
    print(resp)
    await client.session.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
