from unittest.mock import MagicMock, Mock
import pytest
import json
import os

# Helper method for getting JSONs from tests/data folder
@pytest.fixture()
def load_data():
    def load(file_name):
        with open(os.path.join('tests/data/', file_name)) as f:
            return json.load(f)
    return load

# Helper method for returning mock responses via requests module
@pytest.fixture()
def mock_request():
    def mock(data):
        class Response:
            def __init__(self, data):
                self.status_code = 200
                self.text = json.dumps(data)
        return lambda *args, **kwargs: Response(data)
    return mock