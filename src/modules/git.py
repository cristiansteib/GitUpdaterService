import subprocess
import os


class runCommand:

    @staticmethod
    def execute(*command):
        """ return the stored the output"""
        return subprocess.check_output(list(command))

    @staticmethod
    def os_run(command):
        retcode = os.system(command)
        return retcode


def save_and_restore_dir(func):
    """ decorator just for changhe old directory and restore"""

    def func_wrapper(self):
        old_dir = os.getcwd()
        os.chdir(self.path)
        func(self)
        os.chdir(old_dir)

    return func_wrapper


class Git(runCommand):
    def __init__(self, path):
        self.path = path

    def current_branch(self):
        return 'master' #TODO

    @save_and_restore_dir
    def branch(self, name):
        return self.execute('git', 'branch', name)

    @save_and_restore_dir
    def checkout(self, name):
        return self.execute('git', 'checkout', name)

    @save_and_restore_dir
    def update(self):
        return self.execute('git', 'update')

    @save_and_restore_dir
    def fetch(self):
        return self.execute('git', 'fetch')

    @save_and_restore_dir
    def resetHard(self, branch):
        return self.execute('git', 'reset', '--hard', 'origin/' + branch)

    @save_and_restore_dir
    def pull(self, origin='master'):
        return self.execute('git', 'pull', 'origin', origin, '-q')

    @save_and_restore_dir
    def remote_update(self):
        return self.execute('git', 'remote', 'update')

    @save_and_restore_dir
    def is_updated_need_in_current_branch(self, ):
        self.remote_update()
        ex = self.execute('git', 'rev-list', 'HEAD..origin/' + self.current_branch(), '--count')
        return int(ex.decode().strip()) > 0
