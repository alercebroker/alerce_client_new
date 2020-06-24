import requests


class ALeRCE:
    def __init__(self, **kwargs):
        ztf_url = kwargs.get("ztf_url", "3.212.59.238:8082")
        self.config = {"ZTF_API_URL": ztf_url}  ## define default config
        self.session = requests.Session()

    def load_config_from_object(self, config):
        self.config.update(config)

    def load_config_from_file(self, file):
        config = self.parse_config_from_file(file)
        self.config.update(config)

    def parse_config_from_file(self, file):
        ## parse file
        return {}

    @property
    def ztf_url(self):
        return self.config["ZTF_API_URL"]

    def query_objects(self, args):
        return self.session.get("%s/objects" % self.ztf_url, params=args)

    def query_lightcurve(self, oid):
        return self.session.get("%s/objects/%s/lightcurve" % (self.ztf_url, oid))

    def query_detections(self, oid):
        return self.session.get("%s/objects/%s/detections" % (self.ztf_url, oid))
    
    def query_non_detections(self, oid):
        return self.session.get("%s/objects/%s/non_detections" % (self.ztf_url, oid))


