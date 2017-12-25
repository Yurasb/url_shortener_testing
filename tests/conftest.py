import pytest

import test_cases.test_case as cases


@pytest.fixture(scope='function')
def url(request):
    return 'http://localhost:7777/shortcut'


@pytest.fixture(scope='function')
def test_case(request):
    return cases.positive_shortcut
