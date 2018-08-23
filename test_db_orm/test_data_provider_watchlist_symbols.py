from test_db_orm.test_data_provider import *
from data_provider import *


@pytest.mark.usefixtures("reset_db")
class TestWatchlistSymbols(object):

    def test_add_watchlist_symbol(self):
        user_id = 41
        watchlist_name = 'Tech'
        symbol = 'nflx'
        watchlist = get_watchlist(user_id=user_id, watchlist_name=watchlist_name)
        num_of_symbols = len(watchlist.watchlist_items)
        add_watchlist_symbol(watchlist_id=watchlist.id, symbol=symbol)
        watchlist = get_watchlist(user_id=user_id, watchlist_name=watchlist_name)
        assert len(watchlist.watchlist_items) == num_of_symbols + 1

    def test_delete_watchlist_symbol(self):
        user_id = 41
        watchlist_name = 'Tech'
        symbol = 'msft'
        watchlist = get_watchlist(user_id=user_id, watchlist_name=watchlist_name)
        num_of_symbols = len(watchlist.watchlist_items)
        delete_watchlist_symbol(watchlist_id=watchlist.id, symbol=symbol)
        watchlist = get_watchlist(user_id=user_id, watchlist_name=watchlist_name)
        assert len(watchlist.watchlist_items) == num_of_symbols - 1

    def test_get_watchlist_symbols(self):
        user_id = 41
        watchlist_name = 'Tech'
        watchlist = get_watchlist(user_id=user_id, watchlist_name=watchlist_name)
        watchlist_items = get_watchlist_symbols(watchlist_id=watchlist.id)
        for watchlist_item in watchlist_items:
            assert watchlist_item
