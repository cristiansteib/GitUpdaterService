from modules import read_project_config, cli, git
from os import listdir
import subprocess
import os
import logging


class Updater:
    def __init__(self,
                 the_file=None,
                 configs_directory=None,
                 verbose=True,
                 full_verbose=True
                 ):

        self.cli = cli.Cli(verbose=verbose, full_verbose=full_verbose)
        self.path_to_file_to_read = the_file
        self.path_to_multiple_files = configs_directory

    def run(self):
        if self.path_to_file_to_read:
            self.__run_for_single_config(self.path_to_file_to_read)
        elif self.path_to_multiple_files:
            self.__run_for_multiple_configs(self.path_to_multiple_files)

    def run_if_project_exists(self, project):
        if self.path_to_multiple_files:
            self.__run_for_multiple_configs(self.path_to_multiple_files, project)
        else:
            logging.warning("The directory for the configs files was not set")

    def __run_for_single_config(self, the_file):
        self.__run_updater(read_project_config.ConfigReader(os.path.abspath(the_file)))

    def __run_for_multiple_configs(self, directory, only_this_project=None):
        configs_files = listdir(directory)
        directory = os.path.abspath(directory)
        for the_file in configs_files:
            abs_path = os.path.join(directory, the_file)
            config_of_project = read_project_config.ConfigReader(abs_path)
            if (only_this_project and only_this_project == config_of_project.get_project_name()) ^ (not config_of_project.is_webhook):
                self.__run_updater(config_of_project)


    def run_command(self,command):
        """ run and wait to finish"""
        if command and len(command) > 0:
            self.cli.info('About to run: %s' % command)
            process = subprocess.Popen(command, shell=True)
            os.waitpid(process.pid, 0)

    def __run_updater(self, config):
        branch = config.get_branch()
        git_instance = git.Git(config.get_path())

        if git_instance.current_branch() != branch:
            git_instance.checkout(branch)

        if git_instance.current_branch_need_pull():
            # do the update in the repo folder
            self.run_command(config.get_hook_pre())
            self.cli.info('Updating branch {0} for project: {1}'.format(branch, config.get_project_name()))
            git_instance.reset_hard()
            git_instance.pull(branch)
            self.run_command(config.get_hook_post())
        else:
            self.cli.f_info('Branch {0} Up-to-date, for project {1}'.format(branch, config.get_project_name()))