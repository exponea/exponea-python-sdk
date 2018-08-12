from src.client import Exponea
from pytest_mock import mocker

def test_get_customer(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_customer.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    customer = exponea.customer.get_customer({ "registered": "test" })
    assert customer["properties"]["first_name"] == "Lukas"
    assert customer["ids"]["registered"] == "test"
    assert customer["events"][0] == {
          "properties": {
            "foo": "bar"
          },
          "timestamp":1533495544.343536,
          "type":"test"
    }

def test_get_customer_consents(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_customer_consents.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    consents = exponea.customer.get_customer_consents({ "registered": "test" }, [ "newsletter" ])
    assert consents["newsletter"] == False


def test_get_customer_attributes(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_customer_attributes.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    customer = exponea.customer.get_customer_attributes({ "registered": "test" }, ids=["id"], segmentations=["segm"], aggregations=["aggr"], properties=["prop"])
    assert customer["properties"]["prop"] == "Lukas"
    assert customer["ids"]["id"] == ["123"]
    assert customer["aggregations"]["aggr"] == 0
    assert customer["segmentations"]["segm"] == "not_bought"

def test_get_customers(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_customers.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    customers = exponea.customer.get_customers()
    assert customers[0] == {
        "ids": {
            "registered": "test",
            "cookie": [ "cookie" ]
        },
        "properties": {
            "first_name": "Lukas",
            "last_name": "Cerny"
        }
    }

def test_get_events(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_events.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    events = exponea.customer.get_events({ "registered": "test"}, [ "test" ])
    assert events[0] == {
        "properties":{
            "test": "foo"
        },
        "timestamp":1533495529.9268496,
        "type":"test"
    }

            
