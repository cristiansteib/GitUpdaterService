from decorators.singleton import SingletonDecorator


@SingletonDecorator
class Cli:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def log(self, msg):
        if self.verbose:
            print(msg)

    def warning(self):
        pass

    def info(self,msg):
        if self.verbose:
            print(msg)

    def error(self, msg):
        print(msg)

