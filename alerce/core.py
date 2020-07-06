from .search import AlerceSearch
from .crossmatch import AlerceXmatch
from .stamps import AlerceStamps


class Alerce(AlerceSearch, AlerceXmatch, AlerceStamps):
    def __init__(self, **kwargs):
       super().__init__(**kwargs) 

    def load_config_from_file(self, path):
        pass

    def load_config_from_object(self, object):
        super().load_config_from_object(object)
