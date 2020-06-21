from db_plugins.db import SQLDatabase
from object_query import SQLObjectQuery


class ALeRCE:
    def __init__(self):
        self.config = {}  ## define default config
        self.sql_db = SQLDatabase()

    def load_config_from_object(self, config):
        self.config.update(config)

    def load_config_from_file(self, file):
        config = self.parse_config_from_file(file)
        self.config.update(config)

    def parse_config_from_file(self, file):
        ## parse file
        return {}

    def init_client(self):
        self.sql_db.connect(config=self.config["DATABASE"]["SQL"])

    def query_objects(self, args):
        return SQLObjectQuery(self.sql_db).query_objects(args)
