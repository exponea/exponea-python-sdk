import pytest
import json
import os


@pytest.fixture()
def load_data():
    """Helper method for getting JSONs from tests/data folder"""
    def load(file_name):
        with open(os.path.join('tests/data/', file_name)) as f:
            return json.load(f)

    return load


@pytest.fixture()
def mock_request():
    """Helper method for returning mock responses via requests module"""
    def mock(data):
        class Response:
            def __init__(self, data):
                self.status_code = 200
                self.text = json.dumps(data)

        return lambda *args, **kwargs: Response(data)

    return mock
