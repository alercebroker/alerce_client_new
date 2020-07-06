import json

import requests

from .exceptions import FormatValidationError, ParseError, handle_error
from .utils import Result, Client


class AlerceSearch(Client):
    def __init__(self, **kwargs):
        self.session = requests.Session()
        default_config = {
            "ZTF_API_URL": "http://3.212.59.238:8082",
            "ZTF_ROUTES": {
                "objects": "/objects",
                "single_object": "/objects/%s",
                "detections": "/objects/%s/detections",
                "non_detections": "/objects/%s/non_detections",
                "lightcurve": "/objects/%s/lightcurve",
                "magstats": "/objects/%s/magstats",
                "probabilities": "/objects/%s/probabilities",
            },
        }
        default_config.update(kwargs)
        super().__init__(**default_config)
        self.allowed_formats = ["pandas", "votable", "json"]

    def _request(
        self, method, url, params=None, response_field=None, result_format="json"
    ):
        result_format = self.__validate_format(result_format)
        resp = self.session.request(method, url, params=params)

        if resp.status_code >= 400:
            handle_error(resp)
        if response_field and result_format != "json":
            return Result(resp.json()[response_field], format=result_format)
        return Result(resp.json(), format=result_format)

    @property
    def ztf_url(self):
        return self.config["ZTF_API_URL"]

    def __get_url(self, resource, *args):
        return self.ztf_url + self.config["ZTF_ROUTES"][resource] % args

    def __validate_format(self, format):
        format = format.lower()
        if not format in self.allowed_formats:
            raise FormatValidationError(
                "Format '%s' not in %s" % (format, self.allowed_formats), code=500
            )
        return format

    def query_objects(self, format="pandas", **kwargs):
        if "class_name" in kwargs:
            kwargs["class"] = kwargs.pop("class_name")
        q = self._request(
            "GET",
            url=self.__get_url("objects"),
            params=kwargs,
            result_format=format,
            response_field="items",
        )
        return q.result()

    def query_object(self, oid, format="json"):
        q = self._request("GET", self.__get_url("single_object", oid))
        return q.result()

    def query_lightcurve(self, oid):
        q = self._request("GET", self.__get_url("lightcurve", oid))
        return q.result()

    def query_detections(self, oid):
        q = self._request("GET", self.__get_url("detections", oid))
        return q.result()

    def query_non_detections(self, oid):
        q = self._request("GET", self.__get_url("non_detections", oid))
        return q.result()

    def query_magstats(self, oid):
        q = self._request("GET", self.__get_url("magstats", oid))
        return q.result()

    def query_probabilities(self, oid):
        q = self._request("GET", self.__get_url("probabilities", oid))
        return q.result()
