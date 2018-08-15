import pytest
from data_provider import *
from test_data_provider import *


@pytest.mark.usefixtures("reset_db")
class TestWatchlistSymbols(object):

    def test_get_watchlist_symbols(self):
        pass

    def test_add_watchlist_symbol(self):
        pass

    def test_delete_watchlist_symbol(self):
        pass
