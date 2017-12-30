import pytest

from test_cases.test_case import TEST_SUITE


@pytest.fixture(scope='function', params=['http://localhost:7777/shortcut', 'http://localhost:7777/stats'])
def url(request):
    return request.param


@pytest.fixture(scope='function', params=TEST_SUITE)
def test_case(request):
    return request.param
