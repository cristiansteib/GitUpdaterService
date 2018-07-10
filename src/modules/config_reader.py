"""
This module is only used to read the config for to assist the runner .

"""
try:
    import ConfigParser as configparser
except ImportError:
    import configparser


class ConfigReader:

    def __init__(self, absolute_path):
        self.settings = configparser.ConfigParser(defaults=self.get_defaults())
        self.settings.read(absolute_path)
        self._web_port = None
        self._web_host = None
        self._url_path = None
        self._active_web = None
        self._demonize = None
        self._demonize_interval = None
        self._log_level = None
        self._process_web_service_config()

    def _process_web_service_config(self):
        self._web_port = self.settings.get('web','port')

    @staticmethod
    def get_defaults():
        return {}

    def demonize(self):
        pass

    def active_web(self):
        return self._active_web

    def web_port(self):
        return self._web_port

    def web_host(self):
        return self._web_host

    def configs_directory(self):
        """
        :return: the directory where is located the configs files, for every project
        """
        return ''
