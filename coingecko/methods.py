
class BaseURL:
    BASE: str = "https://api.coingecko.com/api/v3/{}"


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
