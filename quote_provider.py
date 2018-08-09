from quote_config import get_quote


def get_all_quotes(symbols=[]):
    quote_result = []
    if symbols:
        for symbol in symbols:
            symbol_data = get_quote(symbol)
            if symbol_data:
                quote_result.append(symbol_data)
    return quote_result


def get_name_of_symbol(symbol):
    if symbol:
        symbol_data = get_quote()
        if symbol_data:
            return symbol_data['name']
    return None


if __name__ == '__main__':
    print(get_quote("GOOG"))
