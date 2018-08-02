import urllib3
import json

API_URL = "https://quote.cnbc.com/quote-html-webservice/quote.htm?" \
          "partnerId=2&requestMethod=quick&exthrs=1&noform=1&fund=1&" \
          "output=json&symbols={}"


def get_quote(symbol="GOOG"):
    result = None
    if not symbol or symbol == "":
        return result
    try:
        with urllib3.PoolManager() as http:
            url = API_URL.format(symbol.upper())
            # print(url)
            response = http.request('GET', url)
            # print(response.status)
            if response.status == 200:
                quote_data = json.loads(response.data.decode('utf-8'))
                # print(quote_data)
                result = {
                    "symbol": symbol,
                    "change_percent": quote_data["QuickQuoteResult"]["QuickQuote"]["change_pct"],
                    "change": quote_data["QuickQuoteResult"]["QuickQuote"]["change"],
                    "type": quote_data["QuickQuoteResult"]["QuickQuote"]["assetType"],
                    "last_price": quote_data["QuickQuoteResult"]["QuickQuote"]["last"]
                }
    except Exception as e:
        print(e)
    finally:
        http.clear()
        # print("This is the finally block")
        return result
