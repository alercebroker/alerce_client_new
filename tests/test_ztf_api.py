from unittest.mock import Mock, patch
from fixtures import alerce
from requests import Session


@patch.object(Session, "get")
def test_query_objects(mock_get, alerce):
    mock_get.return_value.ok = True
    payload = {"class": "LPV"}
    r = alerce.query_objects(payload)
    assert r is not None


@patch.object(Session, "get")
def test_query_lightcurve(mock_get, alerce):
    mock_get.return_value.ok = True
    r = alerce.query_lightcurve("oid")
    assert r is not None

@patch.object(Session, "get")
def test_query_detections(mock_get, alerce):
    mock_get.return_value.ok = True
    r = alerce.query_detections("oid")
    assert r is not None

@patch.object(Session, "get")
def test_query_non_detections(mock_get, alerce):
    mock_get.return_value.ok = True
    r = alerce.query_non_detections("oid")
    assert r is not None