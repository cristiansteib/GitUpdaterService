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
        self._path_to_one_projects_configs = self.settings.get('Globals', 'path_to_projects_configs')
        self._path_to_one_file = None
        self._web_host = None
        self._demonize = None
        self._demonize_interval = None
        self._log_level = self.settings.get('Globals', 'log_level')
        self._log_file = self.settings.get('Globals', 'log')

        self._web_port = self.settings.get('web', 'port')
        self._active_web = self.settings.get('web', 'active')
        self._url_path = self.settings.get('web', 'path_url')
        self._secret_token = self.settings.get('web', 'secret_token')


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

    def path_to_projects_configs(self):
        """
        :return: the directory where is located the configs files, for every project
        """
        return self._path_to_one_projects_configs

    def path_to_one_file(self):
        return self._path_to_one_file

    def verbose(self):
        return True

    def set_path_to_one_file(self, config_file):
        self._path_to_one_file = config_file

    def set_path_to_projects_configs(self, configs_directory):
        self._path_to_one_projects_configs = configs_directory

    def set_active_web(self, web):
        self._active_web = web

    def url_path(self):
        return self._url_path

    def log_file(self):
        return self._log_file

    def log_level(self):
        return self._log_level
