"""
This module is only used to read the config for to assist the runner .

"""


class ReadConfig:

    def __init__(self):
        self.port = None
        self.url_path = None
        self.active_web = None
        self.demonize = None
        self.demonize_interval = None
        self.log_level = None

    def demonize(self):
        pass

    def web_service(self):
        pass

    def web_port(self):
        pass