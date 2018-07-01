from src.decorators.singleton import SingletonDecorator

@SingletonDecorator
class Cli:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def log(self, msg):
        if self.verbose:
            print(msg)
