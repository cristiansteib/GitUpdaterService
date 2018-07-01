try:
    import ConfigParser
except:
    import configparser as ConfigParser


class ConfigReader:
    def __init__(self, the_file):
        self.settings = ConfigParser.SafeConfigParser(self.get_defaults())
        self.settings.read(the_file)
        self.sections = self.settings.sections()
        self.current_section = self.sections[0]  # casi hardcoded section. FIXME

    @staticmethod
    def get_defaults():
        return {
            'pre_update': None,
            'post_update': None
        }

    def get_branch(self):
        return self.settings.get(self.current_section, 'branch')

    def get_path(self):
        return self.settings.get(self.current_section, 'path')

    def get_hook_pre(self):
        return self.settings.get(self.current_section, 'pre_update')

    def get_hook_post(self):
        return self.settings.get(self.current_section, 'post_update')

    def get_project_name(self):
        return self.current_section