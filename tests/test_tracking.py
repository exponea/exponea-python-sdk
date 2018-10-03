from exponea_python_sdk.client import Exponea


def test_get_system_time(mocker, load_data, mock_request):
    exponea = Exponea('test')
    mock_exponea_response = load_data('test_system_time.json')
    mocker.patch('requests.request', mock_request(mock_exponea_response))
    time = exponea.tracking.get_system_time()
    assert time == 1533663283.8943756


def test_update_customer_properties(mocker, load_data, mock_request):
    exponea = Exponea('test')
    mock_exponea_response = load_data('test_tracking.json')
    mocker.patch('requests.request', mock_request(mock_exponea_response))
    response = exponea.tracking.update_customer_properties({'registered': 'foo'}, {'foo': 'bar'})
    assert response is True


def test_add_event(mocker, load_data, mock_request):
    exponea = Exponea('test')
    mock_exponea_response = load_data('test_tracking.json')
    mocker.patch('requests.request', mock_request(mock_exponea_response))
    response = exponea.tracking.add_event({'registered': 'foo'}, {'foo': 'bar'})
    assert response is True


def test_batch_commands(mocker, load_data, mock_request):
    exponea = Exponea('test')
    mock_exponea_response = load_data('test_batch_command.json')
    mocker.patch('requests.request', mock_request(mock_exponea_response))
    response = exponea.tracking.batch_commands([
        exponea.tracking.add_event({'registered': 'test'}, 'test', batch=True),
        exponea.tracking.update_customer_properties({'registered': 'test'}, {'first_name': 'test'}, batch=True),
        exponea.tracking.get_system_time(batch=True)
    ])
    assert response[0] is True
    assert response[1] is True
    assert response[2] == 1533833360.2316685
