from modules import read_config, cli, git
from os import listdir
import subprocess
import os


class Updater:
    def __init__(self,
                 the_file=None,
                 configs_directory=None,
                 verbose=True
                 ):

        self.cli = cli.Cli(True)

        if the_file:
            self.__run_for_single_config(the_file)
        elif configs_directory:
            self.__run_for_multiple_configs(configs_directory)

    def __run_for_single_config(self, the_file):
        self.__run_updater(read_config.ConfigReader(the_file))

    def __run_for_multiple_configs(self, directory):
        configs_files = listdir(directory)
        for the_file in configs_files:
            self.__run_updater(read_config.ConfigReader(the_file))

    @staticmethod
    def run_command(command):
        """ run and wait to finish"""
        if command and len(command) > 0:
            process = subprocess.Popen(command, shell=True)
            os.waitpid(process.pid, 0)

    def __run_updater(self, config):
        self.run_command(config.get_hook_pre())

        branch = config.get_branch()

        gitt = git.Git(config.get_path())
        ex = gitt.remote_update()

        if gitt.is_updated_need_in_current_branch():
            # do the update
            self.cli.info("Updating branch %s" % branch)
            ex = gitt.pull(branch)
            self.run_command(config.get_hook_post())




u = Updater(the_file='project_configs/unAventon.conf')
