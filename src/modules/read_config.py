from ConfigParser import ConfigParser


class ConfigReader:
    def __init__(self, the_file):
        self.configParse = ConfigParser()
        self.configParse.read(the_file)
        self.sections = self.configParse.sections()

    @staticmethod
    def get_configs(folder):
        return