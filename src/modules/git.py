import subprocess
import os


class runCommand:

    def execute(self, *command):
        """ return the stored the output"""
        return subprocess.check_output(list(command), cwd=self.path)

    @staticmethod
    def os_run(command):
        retcode = os.system(command)
        return retcode


class Git(runCommand):
    def __init__(self, path):
        self.path = path

    def current_branch(self):
        return 'master' #TODO

    def branch(self, name):
        return self.execute('git', 'branch', name)

    def checkout(self, name):
        return self.execute('git', 'checkout', name)

    def update(self):
        return self.execute('git', 'update')

    def fetch(self):
        return self.execute('git', 'fetch')

    def resetHard(self, branch):
        return self.execute('git', 'reset', '--hard', 'origin/' + branch)

    def pull(self, origin='master'):
        return self.execute('git', 'pull', '--no-edit', 'origin', origin, '-q')

    def remote_update(self):
        return self.execute('git', 'remote', 'update')

    def is_updated_need_in_current_branch(self, ):
        self.remote_update()
        ex = self.execute('git', 'rev-list', 'HEAD..origin/' + self.current_branch(), '--count')
        return int(ex.decode().strip()) > 0
