import pytest

from exponea_python_sdk.client import Exponea
from exponea_python_sdk.exceptions import APIException


def test_access_key_not_found_exception(mocker, mock_request):
    exponea = Exponea('test')
    response = {
        'error': 'access key not found',
        'success': False
    }
    mocker.patch('requests.request', mock_request(response))
    with pytest.raises(APIException) as exception:
        exponea.analyses.get_report('test')
    assert 'access key not found' in str(exception.value)


def test_not_authorized_exception(mocker, mock_request):
    exponea = Exponea('test')
    response = {
        'errors': ['not authorized to update specified customer properties'],
        'success': False
    }
    mocker.patch('requests.request', mock_request(response))
    with pytest.raises(APIException) as exception:
        exponea.analyses.get_report('test')
    assert 'not authorized to update specified customer properties' in str(exception.value)


def test_errors_global_exception(mocker, mock_request):
    exponea = Exponea('test')
    response = {
        'errors': {'_global': ['Customer does not exist']},
        'success': False
    }
    mocker.patch('requests.request', mock_request(response))
    with pytest.raises(APIException) as exception:
        exponea.customer.get_customer({'registered': 'test'})
    assert 'Customer does not exist' in str(exception.value)


def test_no_permission_to_retrieve_attribute(mocker, mock_request):
    exponea = Exponea('test')
    response = {
        'results': [{'value': 'Lukas', 'success': True}, {'error': 'No permission', 'success': False},
                    {'value': 'not bought', 'success': True}],
        'success': True
    }
    mocker.patch('requests.request', mock_request(response))
    attributes = exponea.customer.get_customer_attributes({'registered': 'test'}, ids=['test'], properties=['name'],
                                                          expressions=['test'])
    assert attributes['ids']['test'] is None
    assert attributes['properties']['name'] == 'Lukas'
    assert attributes['expressions']['test'] == 'not bought'
