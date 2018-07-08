"""
This module is only used to read the config for to assist the runner .

"""


class ConfigReader:

    def __init__(self):
        self.web_port = None
        self.web_host = None
        self.url_path = None
        self.active_web = None
        self.demonize = None
        self.demonize_interval = None
        self.log_level = None

    def demonize(self):
        pass

    def active_web(self):
        return self.active_web

    def web_port(self):
        return self.web_port

    def web_host(self):
        return self.web_host

    def configs_directory(self):
        """
        :return: the directory where is located the configs files, for every project
        """
        return ''