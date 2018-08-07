from Exponea import Exponea
from pytest_mock import mocker

def test_get_system_time(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_system_time.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    time = exponea.Tracking.get_system_time()
    assert time == 1533663283.8943756

def test_update_customer_properties(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_tracking.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    response = exponea.Tracking.update_customer_properties({ "registered": "foo" }, { "foo": "bar" })
    assert response == True

def test_add_event(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_tracking.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    response = exponea.Tracking.add_event({ "registered": "foo" }, { "foo": "bar" })
    assert response == True

def test_batch_commands(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_tracking.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    response = exponea.Tracking.batch_commands({ "registered": "foo" })
    assert response == True