from quote_config import get_quote


def get_all_quotes(symbols=[]):
    quote_result = []
    if symbols:
        for symbol in symbols:
            symbol_data = get_quote(symbol)
            if symbol_data:
                quote_result.append(symbol_data)
        return quote_result
    return quote_result


if __name__ == '__main__':
    print(get_quote("GOOG"))
