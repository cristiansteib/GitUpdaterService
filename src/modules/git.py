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
        # todo: make it re expression
        out = self.execute('git', 'branch').decode()
        branch = list(filter(lambda x: x.startswith('* '), out.split('\n')))[0][2:]
        return branch

    def branch(self, name):
        return self.execute('git', 'branch', name)

    def checkout(self, name):
        return self.execute('git', 'checkout', name)

    def update(self):
        return self.execute('git', 'update')

    def fetch(self):
        return self.execute('git', 'fetch', '-q')

    def fetch_branch(self, branch):
        if self.current_branch() != branch:
            branch = branch + ':' + branch
        return self.execute('git', 'fetch', 'origin', branch, '-q')

    def reset_hard(self):
        return self.execute('git', 'reset', '--hard')

    def pull(self, origin='master'):
        return self.execute('git', 'pull', '--no-edit', 'origin', origin, '--quiet')

    def diff_local_vs_remote(self, branch):
        return self.execute('git', 'diff', '--name-only', branch, 'origin/' + branch)

    def remote_update(self):
        return self.execute('git', 'remote', 'update')

    def current_branch_need_pull(self):
        self.fetch_branch(self.current_branch())
        local = self.execute('git', 'rev-parse', '@')
        remote = self.execute('git', 'rev-parse', '@{u}')
        base = self.execute('git', 'merge-base', '@', '@{u}')
        if local == remote:
            return False
        return local == base
