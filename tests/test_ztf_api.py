from unittest.mock import Mock, patch
from fixtures import alerce
from requests import Session


@patch.object(Session, "request")
def test_query_objects(mock_request, alerce):
    mock_request.return_value.status_code = 200
    r = alerce.query_objects(classifier="late")
    assert r is not None


@patch.object(Session, "request")
def test_query_object(mock_request, alerce):
    mock_request.return_value.status_code = 200
    r = alerce.query_object("oid")
    assert r is not None


@patch.object(Session, "request")
def test_query_lightcurve(mock_request, alerce):
    mock_request.return_value.status_code = 200
    r = alerce.query_lightcurve("oid")
    assert r is not None


@patch.object(Session, "request")
def test_query_detections(mock_request, alerce):
    mock_request.return_value.status_code = 200
    r = alerce.query_detections("oid")
    assert r is not None


@patch.object(Session, "request")
def test_query_non_detections(mock_request, alerce):
    mock_request.return_value.status_code = 200
    r = alerce.query_non_detections("oid")
    assert r is not None


@patch.object(Session, "request")
def test_query_magstats(mock_request, alerce):
    mock_request.return_value.status_code = 200
    r = alerce.query_magstats("oid")
    assert r is not None


@patch.object(Session, "request")
def test_query_probabilities(mock_request, alerce):
    mock_request.return_value.status_code = 200
    r = alerce.query_probabilities("oid")
    assert r is not None
