verbose = False

class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance == None:
            self.instance = self.klass(*args, **kwds)
        return self.instance


@SingletonDecorator
class Cli:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def log(self, msg):
        if self.verbose:
            print(msg)
