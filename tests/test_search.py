from unittest.mock import Mock, patch
from requests import Session
from requests import Response
from pandas import DataFrame
from astropy.table import Table
import sys
import pytest

sys.path.append("..")
from alerce.core import Alerce
from alerce.exceptions import ObjectNotFoundError, FormatValidationError, ParseError

alerce = Alerce()


@patch.object(Session, "request")
def test_query_objects(mock_request):
    mock_request.return_value.status_code = 200
    r = alerce.query_objects(classifier="late")
    assert r is not None


@patch.object(Session, "request")
def test_query_objects_not_found(mock_request):
    mock_request.return_value.status_code = 404
    with pytest.raises(ObjectNotFoundError):
        alerce.query_objects(classifier="late")


@patch.object(Session, "request")
def test_query_objects_parser_error(mock_request):
    mock_request.return_value.status_code = 400
    with pytest.raises(ParseError):
        alerce.query_objects(classifier=123)


@patch.object(Session, "request")
def test_query_objects_format_error(mock_request):
    mock_request.return_value.status_code = 400
    with pytest.raises(FormatValidationError):
        alerce.query_objects(format="not_allowed_format")


@patch.object(Session, "request")
def test_query_objects_format_pandas(mock_request):
    mock_request.return_value.status_code = 200
    r = alerce.query_objects(format="pandas")
    assert isinstance(r, DataFrame)

@patch.object(Session, "request")
def test_query_objects_format_json(mock_request):
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = "ok"
    r = alerce.query_objects(format="json")
    assert r == "ok"

@patch.object(Session, "request")
def test_query_objects_format_votable(mock_request):
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = {"items": {}}
    r = alerce.query_objects(format="votable")
    assert isinstance(r, Table)


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
