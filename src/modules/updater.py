from . import read_config, cli, git
from os import listdir
import subprocess
import os


class Updater:
    def __init__(self,
                 the_file=None,
                 configs_directory=None,
                 verbose=True,
                 full_verbose=True
                 ):

        self.cli = cli.Cli(verbose=verbose, full_verbose=full_verbose)
        if the_file:
            self.__run_for_single_config(the_file)
        elif configs_directory:
            self.__run_for_multiple_configs(configs_directory)

    def __run_for_single_config(self, the_file):
        self.__run_updater(read_config.ConfigReader(os.path.abspath(the_file)))

    def __run_for_multiple_configs(self, directory):
        configs_files = listdir(directory)
        directory = os.path.abspath(directory)
        for the_file in configs_files:
            abs_path = os.path.join(directory, the_file)
            self.__run_updater(read_config.ConfigReader(abs_path))

    def run_command(self,command):
        """ run and wait to finish"""
        if command and len(command) > 0:
            self.cli.info('About to run: %s' % command)
            process = subprocess.Popen(command, shell=True)
            os.waitpid(process.pid, 0)


    def __run_updater(self, config):

        branch = config.get_branch()
        gitt = git.Git(config.get_path())

        if gitt.is_updated_need_in_current_branch():
            # do the update
            self.run_command(config.get_hook_pre())
            self.cli.info('Updating branch {0} for project: {1}'.format(branch, config.get_project_name()))
            gitt.pull(branch)
            self.run_command(config.get_hook_post())
        else:
            self.cli.f_info('Branch {0} Up-to-date, for project {1}'.format(branch, config.get_project_name()))
