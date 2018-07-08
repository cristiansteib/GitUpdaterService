from modules.updater import Updater
from modules.arguments import parse_args
from time import sleep
from modules import web_server
from modules.config_reader import ConfigReader
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
    def __init__(self, *args, **kgargs):
        threading.Thread.__init__(self)
        self.args = args
        self.kwargs = kgargs

    def run(self):
        web_server.run(*self.args, **self.kwargs)


if __name__ == "__main__":
    config = ConfigReader()
    web_thread = WebThread(
        port=config.web_port
    )

    if config.active_web:
        web_thread.start()

    if len(sys.argv) == 1:
        # no parameter was send, so use the config files
        pass
    else:
        web_thread.start()
        updater = TheUpdater(parse_args())
        updater.run()
