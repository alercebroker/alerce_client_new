import pandas as pd


class Result:
    def __init__(self, json_result, format="json"):
        self.json_result = json_result
        self.format = format

    def to_pandas(self):
        if isinstance(self.json_result, list):
            return pd.DataFrame(self.json_result)
        else:
            return pd.DataFrame([self.json_result])

    def to_votable(self):
        pass

    def to_json(self):
        return self.json_result

    def result(self):
        if self.format == "json":
            return self.to_json()
        if self.format == "pandas":
            return self.to_pandas()
        if self.format == "votable":
            return self.to_votable()

class Client:
    def __init__(self, **kwargs):
        self.config = {}
        self.config.update(kwargs)

    def load_config_from_file(self, path):
        pass

    def load_config_from_object(self, object):
        self.config.update(object)