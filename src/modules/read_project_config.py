"""

This module is only used to read the config of one file, for a project.

A config file example:

        [ProjectName]
        path=/absolute/path/to/project
        branch=master
        pre_update=echo "Hello World" > ~/file.file
        post_update=echo "update done" >> ~/file.file

"""

from .cli import Cli

try:
    import ConfigParser
except:
    import configparser as ConfigParser


class ConfigReader:
    def __init__(self, abs_path_to_file):
        self.cli = Cli()
        self.cli.f_info('Reading config: %s' % abs_path_to_file)
        self.settings = ConfigParser.SafeConfigParser(self.get_defaults())
        self.settings.read(abs_path_to_file)
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
