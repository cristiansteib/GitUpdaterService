from .singleton import SingletonDecorator


@SingletonDecorator
class Cli:
    def __init__(self, verbose=False, full_verbose=False):
        self.verbose = verbose
        self.full_verbose = full_verbose

    def __show(self):
        return self.verbose or self.full_verbose

    def log(self, msg):
        if self.__show():
            print("[LOG] : " + msg)

    def warning(self, msg):
        if self.__show():
            print("[WARNING] : " + msg)

    def info(self, msg):
        if self.__show():
            print("[INFO] : " + msg)

    def f_info(self, msg):
        if self.full_verbose:
            print("[F_INFO] : " + msg)

    def error(self, msg):
        if self.__show():
            print("[ERROR] : " + msg)
