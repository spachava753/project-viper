from test_db_orm.test_data_provider import *
from data_provider import *


@pytest.mark.usefixtures("reset_db")
class TestWatchlist(object):

    def test_get_watchlists_by_id(self):
        watchlist = get_watchlist(watchlist_id=1)
        assert isinstance(watchlist, object)
        assert watchlist.name == 'Tech'

    def test_get_watchlists_by_name(self):
        watchlist = get_watchlist(user_id=41, watchlist_name='Tech')
        assert isinstance(watchlist, object)
        assert watchlist.id == 1

    def test_add_watchlists(self):
        user_id = 41
        new_watchlist_name = 'BlueChip'
        new_watchlist_desc = 'All the bluechip companies'
        original_len = len(get_watchlist(user_id=user_id))
        add_watchlist(new_watchlist_name, new_watchlist_desc, user_id)
        assert len(get_watchlist(user_id=user_id)) == original_len + 1
        watchlists = get_watchlist(user_id=user_id)
        for watchlist in watchlists:
            print(watchlist.name)

    def test_delete_watchlists(self):
        pass
