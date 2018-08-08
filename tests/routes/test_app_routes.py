import pytest

from app import app

def test_index_route():
    testApp = app.test_client()

    #How necessary is this line?
    testApp.testing = True

    result = testApp.get('/')
    assert result.data == b"Hello!"