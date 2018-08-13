from exponea_python_sdk.client import Exponea
from pytest_mock import mocker

def test_get_funnel(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_funnel.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    funnel = exponea.analyses.get_funnel("test")
    assert funnel["name"] == "test_funnel"
    assert funnel["data"][0] == {
        "serie": "Total",
        "step 1 first_session count": 2,
        "step 2 session_start count": 1,
        "step 2 session_start duration from previous": 435764.1615576744
    }
    assert funnel["data"][1] == {
        "serie": "Foo",
        "step 1 first_session count": 1,
        "step 2 session_start count": 1,
        "step 2 session_start duration from previous": 435764.1615576744
    }

def test_get_report(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_report.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    report = exponea.analyses.get_report("test")
    assert report["name"] == "test_report"
    assert report["data"][0] == {
        "cookie id": "test1",
        "count(customer)": 1
    }
    assert report["data"][1] == {
        "cookie id": "test2",
        "count(customer)": 2
    }

def test_get_segmentation(mocker, load_data, mock_request):
    exponea = Exponea("test")
    mock_exponea_response = load_data("test_segmentation.json")
    mocker.patch("requests.request", mock_request(mock_exponea_response))
    segmentation = exponea.analyses.get_segmentation("test")
    assert segmentation["name"] == "test_segmentation"
    assert segmentation["data"][0] == {
        "segment": "already_bought",
        "#": 0
    }
    assert segmentation["data"][1] == {
        "segment": "not_bought",
        "#": 4
    }
            
