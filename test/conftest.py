import pytest
from requests_html import HTMLSession

@pytest.fixture()
def client():
    client = HTMLSession()
    return client
