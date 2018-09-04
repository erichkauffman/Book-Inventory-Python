import pytest

from app import app

def test_index_route():
    testApp = app.test_client()

    result = testApp.get('/')
    assert result.data == b"Hello!"
