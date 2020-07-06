from unittest.mock import Mock, patch
from requests import Session
import sys

sys.path.append("..")
from alerce.core import Alerce

alerce = Alerce()


@patch.object(Session, "request")
def test_query_objects(mock_request):
    mock_request.return_value.status_code = 200
    r = alerce.query_objects(classifier="late")
    assert r is not None


@patch.object(Session, "request")
def test_query_object(mock_request):
    mock_request.return_value.status_code = 200
    r = alerce.query_object("oid")
    assert r is not None


@patch.object(Session, "request")
def test_query_lightcurve(mock_request):
    mock_request.return_value.status_code = 200
    r = alerce.query_lightcurve("oid")
    assert r is not None


@patch.object(Session, "request")
def test_query_detections(mock_request):
    mock_request.return_value.status_code = 200
    r = alerce.query_detections("oid")
    assert r is not None


@patch.object(Session, "request")
def test_query_non_detections(mock_request):
    mock_request.return_value.status_code = 200
    r = alerce.query_non_detections("oid")
    assert r is not None


@patch.object(Session, "request")
def test_query_magstats(mock_request):
    mock_request.return_value.status_code = 200
    r = alerce.query_magstats("oid")
    assert r is not None


@patch.object(Session, "request")
def test_query_probabilities(mock_request):
    mock_request.return_value.status_code = 200
    r = alerce.query_probabilities("oid")
    assert r is not None
