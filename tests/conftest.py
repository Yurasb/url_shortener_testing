from datetime import datetime
import pytest

from tests import helpers


@pytest.fixture(autouse=True)
def remove_all_links(request):
    helpers.purge_db()


@pytest.fixture
def create_shortcut(request):
    helpers.insert_in_db(
        {
            'link': 'http://google.com',
            'lid': 'test_id',
            'r_count': 0,
            'r_at': None
        }
    )


@pytest.fixture
def create_shortcut_redirected(request):
    helpers.insert_in_db(
        {
            'link': 'http://google.com',
            'lid': 'test_id',
            'r_count': 1,
            'r_at': datetime.utcnow()
        }
    )
