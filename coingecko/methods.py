
class BaseURL:
    BASE: str = "https://api.coingecko.com/api/v3/{method}"


class Ping:
    """
    GET /ping Check API server status"""
    PING: str = "ping"


class Simple:
    """
    GET /simple/price Get the current price of any cryptocurrencies in any other supported currencies that you need.
    GET /simple/token_price/{id} Get current price of tokens (using contract addresses) for a given platform in any
    other currency that you need.
    GET /simple/supported_vs_currencies Get list of supported_vs_currencies."""
    PRICE: str = "simple/price"
    TOKEN_PRICE: str = "simple/token_price/{id}"
    SUPPORTED_VS_CURRENCIES: str = "simple/supported_vs_currencies"


class Coins:
    """
    GET /coins/list List all supported coins id, name and symbol (no pagination required)
    GET /coins/markets List all supported coins price, market cap, volume, and market related data
    GET /coins/{id} Get current data (name, price, market, ... including exchange tickers) for a coin
    GET /coins/{id}/tickers Get coin tickers (paginated to 100 items)
    GET /coins/{id}/history Get historical data (name, price, market, stats) at a given date for a coin
    GET /coins/{id}/market_chart Get historical market data include price, market cap, and 24h volume (granularity auto)
    GET /coins/{id}/market_chart/range Get historical market data include price, market cap, and 24h volume within a
    range of timestamp (granularity auto)
    GET /coins/{id}/status_updatesGet status updates for a given coin (beta)
    GET /coins/{id}/ohlc Get coin's OHLC (Beta)
    """
    LIST: str = "/coins/list"
    MARKETS: str = "/coins/markets"
    COIN_DATA: str = "coins/{id}"
    COIN_TICKERS: str = "/coins/{id}/tickers"
    HISTORICAL_DATA: str = "/coins/{id}/history"
    MARKET_CHART: str = "/coins/{id}/market_chart"
    MARKET_CHART_RANGE: str = "/coins/{id}/market_chart/range"
    STATUS_UPDATE: str = "/coins/{id}/status_updates"
    OHLC: str = "/coins/{id}/ohlc"


class Contract:
    """
    GET /coins/{id}/contract/{contract_address} Get coin info from contract address

    GET /coins/{id}/contract/{contract_address}/market_chart/ Get historical market data include price, market cap, and
    24h volume (granularity auto) from a contract address

    GET /coins/{id}/contract/{contract_address}/market_chart/range Get historical market data include price, market cap,
     and 24h volume within a range of timestamp (granularity auto) from a contract address
 """
    COIN_INFO: str = "/coins/{id}/contract/{contract_address}"
    HISTORICAL_DATA: str = "/coins/{id}/contract/{contract_address}/market_chart/"
    HISTORICAL_DATA_RANGE: str = "/coins/{id}/contract/{contract_address}/market_chart/range"


class Exchanges:
    """
    Beta
    GET /exchanges List all exchanges
    GET /exchanges/list List all supported markets id and name (no pagination required)
    GET /exchanges/{id} Get exchange volume in BTC and top 100 tickers only
    GET /exchanges/{id}/tickers Get exchange tickers (paginated, 100 tickers per page)
    GET /exchanges/{id}/status_updates Get status updates for a given exchange (beta)
    GET /exchanges/{id}/volume_chart Get volume_chart data for a given exchange (beta)
    """
    LIST_ALL_EXCHANGES: str = "/exchanges"
    LIST_ALL_SUPPORTED_MARKETS: str = "/exchanges/list"
    EXCHANGE_VOLUME: str = "/exchanges/{id}"
    EXCHANGE_TICKERS: str = "/exchanges/{id}/tickers"
    STATUS_UPDATES: str = "/exchanges/{id}/status_updates"
    VOLUME_CHART: str = "/exchanges/{id}/volume_chart"


class Finance:
    """
    Beta
    GET /finance_platforms List all finance platforms
    GET /finance_products List all finance products
    """
    FINANCE_PLATFORMS: str = "/finance_platforms"
    FINANCE_PRODUCTS: str = "/finance_products"


class Indexes:
    """
    Beta
    GET /indexes List all market indexes
    GET /indexes/{market_id}/{id} get market index by market id and index id
    GET /indexes/list list market indexes id and name
    GET /indexes/list_by_market_and_id/{market_id}/{id} get market index by market id and market index id
    """
    ALL_MARKET_INDEXES: str = "/indexes"
    MARKET_INDEX: str = "/indexes/{market_id}/{id}"
    LIST_MARKET_INDEXES_ID_AND_NAME: str = "/indexes/list"
    MARKET_INDEX_BY_ID_AND_INDEX: str = "/indexes/list_by_market_and_id/{market_id}/{id}"


class Derivatives:
    """
    Beta
    GET /derivatives List all derivative tickers
    GET /derivatives/exchanges List all derivative exchanges
    GET /derivatives/exchanges/{id} show derivative exchange data
    GET /derivatives/exchanges/list List all derivative exchanges name and identifier
    """
    DERIVATIVES_TICKERS: str = "/derivatives"
    DERIVATIVES_EXCHANGES: str = "/derivatives/exchanges"
    DERIVATIVE_EXCHANGE_DATA: str = "/derivatives/exchanges/{id}"
    DERIVATIVE_EXCHANGES_NAME_IDENTIFIER: str = "/derivatives/exchanges/list"


class StatusUpdates:
    """
    Beta
    GET /status_updates List all status_updates with data (description, category, created_at, user, user_title and pin)
    """
    STATUS_UPDATES_WITH_DATA: str = "/status_updates"


class Events:
    """
    GET /events Get events, paginated by 100
    GET /events/countries Get list of event countries
    GET /events/types Get list of events types
    """
    EVENTS: str = "/events"
    EVENTS_COUNTIES: str = "/events/countries"
    EVENTS_TYPES: str = "/events/types"


class ExchangesRates:
    """
    GET /exchange_rates Get BTC-to-Currency exchange rates
    """
    EXCHANGE_RATES: str = "/exchange_rates"


class Trending:
    """
    GET /search/trending Get trending search coins (Top-7) on CoinGecko in the last 24 hours
    """
    TRENDING_SEARCH_COINS: str = "/search/trending"


class Global:
    """
    GET /global Get cryptocurrency global data
    GET /global/decentralized_finance_defi Get cryptocurrency global decentralized finance(defi) data
    """
    CRYPTOCURRENCY_GLOBAL_DATA: str = "/global"
    CRYPTOCURRENCY_GLOBAL_DATA_DEFI: str = "/global/decentralized_finance_defi"
