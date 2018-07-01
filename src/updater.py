from modules import git

class Updater:
    def __init__(self, git_directory):
        self.git = git.Git(git_directory)



u = Updater('.')
