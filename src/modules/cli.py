from decorators.singleton import SingletonDecorator


@SingletonDecorator
class Cli:
    def __init__(self, verbose=False, full_verbose=False):
        self.verbose = verbose
        self.full_verbose = full_verbose

    def log(self, msg):
        if self.verbose:
            print(msg)

    def warning(self):
        pass

    def info(self, msg):
        if self.verbose:
            print(msg)

    def f_info(self, msg):
        if self.full_verbose:
            self.info(msg)

    def error(self, msg):
        print(msg)
