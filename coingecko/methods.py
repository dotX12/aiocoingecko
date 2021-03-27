
class BaseURL:
    BASE: str = "https://api.coingecko.com/api/v3/{method}"


class Ping:
    PING: str = "ping"


class Simple:
    PRICE: str = "simple/price"
    TOKEN_PRICE: str = "simple/token_price/{id}"
    SUPPORTED_VS_CURRENCIES: str = "simple/supported_vs_currencies"


class Coins:
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
    COIN_INFO: str = "/coins/{id}/contract/{contract_address}"
    HISTORICAL_DATA: str = "/coins/{id}/contract/{contract_address}/market_chart/"
    HISTORICAL_DATA_RANGE: str = "/coins/{id}/contract/{contract_address}/market_chart/range"


class Exchanges:
    LIST_ALL_EXCHANGES: str = "/exchanges"
    LIST_ALL_SUPPORTED_MARKETS: str = "/exchanges/list"
    EXCHANGE_VOLUME: str = "/exchanges/{id}"
    EXCHANGE_TICKERS: str = "/exchanges/{id}/tickers"
    STATUS_UPDATES: str = "/exchanges/{id}/status_updates"
    VOLUME_CHART: str = "/exchanges/{id}/volume_chart"
