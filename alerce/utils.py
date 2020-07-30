from pandas import DataFrame
from astropy.table import Table


class Result:
    def __init__(self, json_result, format="json"):
        self.json_result = json_result
        self.format = format

    def to_pandas(self, index=None, sort=None):
        dataframe = None
        if isinstance(self.json_result, list):
            dataframe = DataFrame(self.json_result)
        else:
            dataframe = DataFrame([self.json_result])
        if sort:
            dataframe.sort_values(sort, inplace=True)
        if index:
            dataframe.set_index(index, inplace=True)
        return dataframe

    def to_votable(self):
        return Table(self.json_result)

    def to_json(self):
        return self.json_result

    def result(self, index=None, sort=None):
        if self.format == "json":
            return self.to_json()
        if self.format == "pandas":
            return self.to_pandas(index, sort)
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
