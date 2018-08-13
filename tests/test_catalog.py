from exponea_python_sdk.client import Exponea
from pytest_mock import mocker

def test_create_catalog(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_create_catalog.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    catalog_id = exponea.catalog.create_catalog("test", ["field_one", "field_two"])
    assert catalog_id == "5bfawefds3a0015e7f0b5"

def test_get_catalog_name(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_get_catalog_name.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    catalog_name = exponea.catalog.get_catalog_name("catalog_id")
    assert catalog_name == "test_catalog"

def test_get_catalog_items(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_catalog_items.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    catalog = exponea.catalog.get_catalog_items("catalog_id")
    assert catalog["matched"] == 1
    assert catalog["matched_limited"] == False
    assert catalog["total"] == 1
    assert catalog["limit"] == 20
    assert catalog["skip"] == 0
    assert catalog["data"][0] == {
        "item_id": "1", 
        "properties": {
            "one": "foo", 
            "two": "bar"
        }
    }


