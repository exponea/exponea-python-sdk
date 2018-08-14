import pytest
from exponea_python_sdk.client import Exponea
from exponea_python_sdk.exceptions import APIException
from pytest_mock import mocker


def test_access_key_not_found_exception(mocker, mock_request):
    exponea = Exponea("test")
    response = {
        "error": "access key not found",
        "success": False
    }
    mocker.patch("requests.request", mock_request(response))
    with pytest.raises(APIException) as exception:
        exponea.analyses.get_report("test")
    assert "access key not found" in str(exception.value)

def test_not_authorized_exception(mocker, mock_request):
    exponea = Exponea("test")
    response = {
        "errors": [
            "not authorized to update specified customer properties"
        ],
        "success": False
    }
    mocker.patch("requests.request", mock_request(response))
    with pytest.raises(APIException) as exception:
        exponea.analyses.get_report("test")
    assert "not authorized to update specified customer properties" in str(exception.value)

def test_errors_global_exception(mocker, mock_request):
    exponea = Exponea("test")
    response = {
        "errors": {
            "_global": [
                "Customer does not exist"
            ]
        }, 
        "success": False
    }
    mocker.patch("requests.request", mock_request(response))
    with pytest.raises(APIException) as exception:
        exponea.customer.get_customer({"registered": "test"})
    assert "Customer does not exist" in str(exception.value)

