import asyncio
from dataclasses import dataclass
from typing import Optional, List, Union
from methods import *
from logs import *
from aiohttp import ClientSession
from REST.decorators import get
from REST.async_base import AsyncClient
from enums import *


class CoinGeckoAPI(AsyncClient):
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

        :param ids: id of coins, comma-separated if querying more than 1 coin *refers to coins/list
        :param vs_currencies: vs_currency of coins, comma-separated if querying more than 1 vs_currency
            *refers to simple/supported_vs_currencies
        :param include_market_cap: true/false to include market_cap, default: false
        :param include_24hr_vol: true/false to include 24hr_vol, default: false
        :param include_24hr_change: true/false to include 24hr_change, default: false
        :param include_last_updated_at: true/false to include last_updated_at of price, default: false
        """

    @get(SimpleURL.TOKEN_PRICE)
    async def get_token_price(self, contract_addresses: str, id: str = 'ethereum', vs_currencies: str = 'usd',
                              include_market_cap: bool = False, include_24hr_vol: bool = False,
                              include_24hr_change: bool = False, include_last_updated_at: bool = False) -> dict:
        """
        Get current price of tokens (using contract addresses)
        for a given platform in any other currency that you need.

        :param contract_addresses: The contract address of tokens, comma separated
        :param id: The id of the platform issuing tokens (Only ethereum is supported for now)
        :param vs_currencies: vs_currency of coins, comma-separated if querying more than 1 vs_currency
            *refers to simple/supported_vs_currencies
        :param include_market_cap: true/false to include market_cap, default: false
        :param include_24hr_vol: true/false to include 24hr_vol, default: false
        :param include_24hr_change: true/false to include 24hr_change, default: false
        :param include_last_updated_at: true/false to include last_updated_at of price, default: false
        """

    @get(SimpleURL.SUPPORTED_VS_CURRENCIES)
    async def get_supported_vs_currencies(self) -> dict:
        """
        Get list of supported_vs_currencies.
        """

    @get(CoinsURL.LIST)
    async def get_coins_list(self, include_platform: bool = True) -> dict:
        """
        List all supported coins id, name and symbol (no pagination required)
        Use this to obtain all the coins’ id in order to make API calls

        :param include_platform: flag to include platform contract addresses (eg. 0x… for Ethereum based tokens).
            valid values: true, false
        """

    @get(CoinsURL.MARKETS)
    async def get_coins_markets(self, ids: str, vs_currency: str = 'usd', category: str = '',
                                order: Union[MarketSortOrder, str] = MarketSortOrder.MARKET_CAP_DESC,
                                per_page: int = 100, page: int = 1, sparkline: bool = False,
                                price_change_percentage: str = '1h,24h,7d') -> list:
        """
        List all supported coins price, market cap, volume, and market related data
        Use this to obtain all the coins market data (price, market cap, volume)

        :param ids: The target currency of market data (usd, eur, jpy, etc.)
        :param vs_currency: The ids of the coin, comma separated crytocurrency symbols (base). refers to /coins/list.
            When left empty, returns numbers the coins observing the params limit and start
        :param category: filter by coin category, only decentralized_finance_defi is supported at the moment
        :param order: valid values: market_cap_desc, gecko_desc, gecko_asc, market_cap_asc, market_cap_desc,
            volume_asc, volume_desc, id_asc, id_desc sort results by field.
        :param per_page: valid values: 1…250 Total results per page
        :param page: Page through results
        :param sparkline: Include sparkline 7 days data (eg. true, false)
        :param price_change_percentage: Include price change percentage in 1h, 24h, 7d, 14d, 30d, 200d, 1y
            (eg. '1h,24h,7d' comma-separated, invalid values will be discarded)
        """

    @get(CoinsURL.COIN_DATA)
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

        :param id: pass the coin id (can be obtained from /coins) eg. bitcoin
        :param localization: Include all localized languages in response (true/false) [default: true]
        :param tickers: Include tickers data (true/false) [default: true]
        :param market_data: Include market_data (true/false) [default: true]
        :param community_data: Include community_data data (true/false) [default: true]
        :param developer_data: Include developer_data data (true/false) [default: true]
        :param sparkline: Include sparkline 7 days data (eg. true, false) [default: false]
        """

    @get(CoinsURL.COIN_TICKERS)
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

        :param id: pass the coin id (can be obtained from /coins/list) eg. bitcoin
        :param exchange_ids: filter results by exchange_ids (ref: v3/exchanges/list)
        :param include_exchange_logo: lag to show exchange_logo
        :param page: Page through results
        :param order: valid values: trust_score_desc (default), trust_score_asc and volume_desc
        :param depth: flag to show 2% orderbook depth. valid values: true, false
        """

    @get(CoinsURL.HISTORICAL_DATA)
    async def get_coin_history_by_id(self,
                                     id: str,
                                     date: str,
                                     localization: str = 'en') -> dict:
        """
        Get historical data (name, price, market, stats) at a given date for a coin
        :param id: pass the coin id (can be obtained from /coins) eg. bitcoin
        :param date: The date of data snapshot in dd-mm-yyyy eg. 30-12-2017
        :param localization: Set to false to exclude localized languages in response
        """

    @get(CoinsURL.MARKET_CHART)
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

    @get(CoinsURL.MARKET_CHART_RANGE)
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

    @get(CoinsURL.STATUS_UPDATE)
    async def get_coin_status_updates_by_id(self, id: str, per_page: int = 100, page: int = 1) -> dict:
        """
        Get status updates for a given coin
        :param id: pass the coin id (can be obtained from /coins) eg. bitcoin
        :param per_page: Total results per page
        :param page: Page through results
        """

    @get(CoinsURL.OHLC)
    async def get_coin_ohlc_by_id(self, id: str, vs_currency: str = 'usd', days: str = '7') -> dict:
        """
        Get coin's OHLC (Beta)
        Candle’s body:
        1 - 2 days: 30 minutes
        3 - 30 days: 4 hours
        31 and before: 4 days

        :param id: pass the coin id (can be obtained from /coins/list) eg. bitcoin
        :param vs_currency: The target currency of market data (usd, eur, jpy, etc.)
        :param days: Data up to number of days ago (1/7/14/30/90/180/365/max)
        """

    @get(ContractURL.COIN_INFO)
    async def get_coin_info_from_contract_address_by_id(self, contract_address: str, id: str = 'ethereum') -> dict:
        """
        Get coin info from contract address
        :param id: Asset platform (only ethereum is supported at this moment)
        :param contract_address: Token’s contract address
        """

    @get(ContractURL.HISTORICAL_DATA)
    async def get_coin_market_chart_from_contract_address_by_id(self, contract_address: str, id: str = 'ethereum',
                                                                vs_currency: str = 'usd', days: str = '1d') -> dict:
        """
        Get historical market data include price, market cap, and 24h volume (granularity auto) from a contract address

        :param id: The id of the platform issuing tokens (Only ethereum is supported for now)
        :param contract_address: Token’s contract address
        :param vs_currency: The target currency of market data (usd, eur, jpy, etc.)
        :param days: Data up to number of days ago (eg. 1,14,30,max)
        """

    @get(ContractURL.HISTORICAL_DATA_RANGE)
    async def get_coin_market_chart_range_from_contract_address_by_id(self, contract_address: str,
                                                                      from_timestamp: int,
                                                                      to_timestamp: int,
                                                                      id: str = 'ethereum',
                                                                      vs_currency: str = 'usd') -> dict:
        """
        Get historical market data include price, market cap, and 24h volume within a range of timestamp
        (granularity auto) from a contract address

        :param contract_address: Token’s contract address
        :param from_timestamp: From date in UNIX Timestamp (eg. 1392577232)
        :param to_timestamp: To date in UNIX Timestamp (eg. 1422577232)
        :param id: The id of the platform issuing tokens (Only ethereum is supported for now)
        :param vs_currency: The target currency of market data (usd, eur, jpy, etc.)
        """

    @get(ExchangesURL.LIST_ALL_EXCHANGES)
    async def get_exchanges_list(self, per_page: int = 100, page: int = 1) -> Union[List[dict]]:
        """
        List all exchanges
        :param per_page: Valid values: 1…250 Total results per page Default value:: 100
        :param page: page through results
        """

    @get(ExchangesURL.LIST_ALL_SUPPORTED_MARKETS)
    async def get_exchanges_id_name_list(self) -> Union[List[dict]]:
        """
        List all supported markets id and name (no pagination required)
        Use this to obtain all the markets’ id in order to make API calls
        """

    @get(ExchangesURL.EXCHANGE_VOLUME)
    async def get_exchanges_by_id(self, id: str):
        """
        Get exchange volume in BTC and top 100 tickers only
        Get exchange volume in BTC and tickers

        IMPORTANT:
        Ticker object is limited to 100 items, to get more tickers, use /exchanges/{id}/tickers
        Ticker is_stale is true when ticker that has not been updated/unchanged from the exchange for a while.
        Ticker is_anomaly is true if ticker’s price is outliered by our system.
        You are responsible for managing how you want to display these information (
        e.g. footnote, different background, change opacity, hide)

        :param id: pass the exchange id (can be obtained from /exchanges/list) eg. binance
        """

    @get(ExchangesURL.EXCHANGE_TICKERS)
    async def get_exchanges_tickers_by_id(self, id: str, coin_ids: str, include_exchange_logo: bool = True,
                                          page: int = 1, depth: bool = True,
                                          order: Union[SortOrder, str] = SortOrder.TRUST_SCORE_DESC) -> dict:
        """
        Get exchange tickers (paginated, 100 tickers per page)
        IMPORTANT:
        Ticker is_stale is true when ticker that has not been updated/unchanged from the exchange for a while.
        Ticker is_anomaly is true if ticker’s price is outliered by our system.
        You are responsible for managing how you want to display these information (e.g. footnote, different background,
        change opacity, hide)

        :param id: pass the exchange id (can be obtained from /exchanges/list) eg. binance
        :param coin_ids: filter tickers by coin_ids (ref: v3/coins/list)
        :param include_exchange_logo: flag to show exchange_logo
        :param page: Page through results
        :param depth: flag to show 2% orderbook depth i.e., cost_to_move_up_usd and cost_to_move_down_usd
        :param order: valid values: trust_score_desc (default), trust_score_asc and volume_desc
        """

    @get(ExchangesURL.STATUS_UPDATES)
    async def get_exchanges_status_updates_by_id(self, id: str, per_page: int = 50, page: int = 1) -> dict:
        """
        Get status updates for a given exchange (beta)

        :param id: pass the exchange id (can be obtained from /exchanges/list) eg. binance
        :param per_page: Total results per page
        :param page: Page through results
        """

    @get(ExchangesURL.VOLUME_CHART)
    async def get_exchanges_volume_chart_by_id(self, id: str, days: int = 14) -> list:
        """
        Get volume_chart data for a given exchange (beta)

        :param id: pass the exchange id (can be obtained from /exchanges/list) eg. binance
        :param days: Data up to number of days ago (eg. 1,14,30)
        """

    @get(FinanceURL.FINANCE_PLATFORMS)
    async def get_finance_platforms(self, per_page: int = 100, page: int = 1) -> list:
        """
        List all finance platforms
        :param per_page: Total results per page
        :param page: page of results (paginated to 100 by default)
        """

    @get(FinanceURL.FINANCE_PRODUCTS)
    async def get_finance_products(self, per_page: int = 100, page: int = 1) -> list:
        """
        List all finance products

        :param per_page: Total results per page
        :param page: page of results (paginated to 100 by default)
        # :param start_at: start date of the financial products  | NOT USABLE IN API
        # :param end_at: end date of the financial products | NOT USABLE IN API
        """

    @get(IndexesURL.ALL_MARKET_INDEXES)
    async def get_indexes(self, per_page: int = 100, page: int = 1) -> list:
        """
        List all market indexes

        :param per_page: Total results per page
        :param page: Page through results
        """

    @get(IndexesURL.MARKET_INDEX)
    async def get_indexes_by_id(self, market_id: str, id: str) -> list:
        """
        Get market index by market id and index id

        :param market_id: pass the market id (can be obtained from /exchanges/list)
        :param id: pass the index id (can be obtained from /indexes/list)
        """
        
    @get(IndexesURL.LIST_MARKET_INDEXES_ID_AND_NAME)
    async def get_indexes_list(self) -> list:
        """
        List market indexes id and name
        """



async def main():
    client = CoinGeckoAPI()
    resp = await client.get_indexes_list()
    print(resp)
    await client.session.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
