from quote_config import get_quote


def get_all_quotes(symbols=[]):
    quote_result = []
    for symbol in symbols:
        quote_result.append(get_quote(symbol))
    return quote_result

if __name__ == '__main__':
    print(get_quote("GOOG"))