from modules.updater import Updater
from modules.arguments import parse_args
from time import sleep
from modules.web_server import WebServer
import sys
import threading

class TheUpdater:
    def __init__(self,
                 parse_args,
                 delay_between_updates=2):

        self.update_kwargs = {
            'the_file': parse_args.ini,
            'configs_directory': parse_args.config_directory,
            'verbose': parse_args.verbose,
            'full_verbose': parse_args.verbose_full
        }

        self.daemonize = parse_args.daemonize
        self.delay_between_updates = delay_between_updates

    def run(self):
        while True:
            Updater(**self.update_kwargs)
            sleep(self.delay_between_updates)


class WebThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        WebServer()


if __name__ == "__main__":
    thread_web = WebThread()

    if len(sys.argv) == 1:
        # use the config files
        pass
    else:
        thread_web.start()
        updater = TheUpdater(parse_args())
        print('run updater')
        updater.run()
