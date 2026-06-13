# onct/economie.py

import requests


BASE_URL = "https://api.twelvedata.com"

STOCK_API_KEY = None

VALID_PERIODS = {
    "30D": 30,
    "100D": 100,
    "1Y": 365,
    "2Y": 730,
}


def set_stock_api_key(api_key):
    """
    Save the stock API key.

    Example:
        set_stock_api_key("your_api_key")
    """

    global STOCK_API_KEY
    STOCK_API_KEY = api_key


def get_stock_api_key():
    """
    Return the stored stock API key.
    """

    return STOCK_API_KEY


def _get_stock_api_key_or_raise():
    api_key = get_stock_api_key()

    if api_key is None:
        raise ValueError("No stock API key found. Use set_stock_api_key() first.")

    return api_key


def _prepare_symbols(symbols):
    if isinstance(symbols, str):
        symbol = symbols.strip().upper()

        if symbol == "":
            raise ValueError("Symbol must be a non-empty string, for example 'META'.")

        return symbol

    if isinstance(symbols, list):
        cleaned_symbols = []

        for symbol in symbols:
            if not isinstance(symbol, str) or symbol.strip() == "":
                raise ValueError(
                    "All symbols must be non-empty strings, for example 'META'."
                )

            cleaned_symbols.append(symbol.strip().upper())

        if len(cleaned_symbols) == 0:
            raise ValueError("Symbol list cannot be empty.")

        return ",".join(cleaned_symbols)

    raise ValueError(
        "Symbols must be a string or a list of strings, for example 'META' or ['META', 'AAPL']."
    )


def _get(endpoint, params):
    api_key = _get_stock_api_key_or_raise()

    params["apikey"] = api_key
    params["format"] = "json"

    url = f"{BASE_URL}/{endpoint}"

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        raise ConnectionError(
            "Could not connect to the stock data API. Check your internet connection."
        ) from error

    data = response.json()

    if isinstance(data, dict) and data.get("status") == "error":
        message = data.get("message", "Unknown API error.")
        raise ValueError(f"Stock data API error: {message}")

    return data


def get_stock_quote(symbols):
    """
    Get the current quote for one or more stock symbols.

    Examples:
        quote = get_stock_quote("META")
        quotes = get_stock_quote(["META", "AAPL", "MSFT"])
    """

    prepared_symbols = _prepare_symbols(symbols)

    params = {
        "symbol": prepared_symbols,
    }

    return _get("quote", params)


def get_stock_history(symbols, period="30D"):
    """
    Get historical stock data for one or more stock symbols.

    Supported periods:
        "30D", "100D", "1Y", "2Y"

    Examples:
        data = get_stock_history("META", period="30D")
        data = get_stock_history(["META", "AAPL"], period="100D")
    """

    if period not in VALID_PERIODS:
        raise ValueError("Invalid period. Use: 30D, 100D, 1Y or 2Y.")

    prepared_symbols = _prepare_symbols(symbols)
    output_size = VALID_PERIODS[period]

    params = {
        "symbol": prepared_symbols,
        "interval": "1day",
        "outputsize": output_size,
    }

    return _get("time_series", params)