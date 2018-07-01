import subprocess
import os

class runCommand:

    @staticmethod
    def execute(*command):
        command = list(command)
        return subprocess.run(command, stdout=subprocess.PIPE)


class Git(runCommand):
    def __init__(self, path):
        os.chdir(path)

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
        return self.execute('git', 'pull', 'origin', origin)