from modules.updater import Updater
from time import sleep
from modules import arguments
from modules.config_reader import ConfigReader
import sys
import threading
import logging

class TheUpdaterDaemon:
    def __init__(self,
                 config,
                 demonize=True,
                 delay_between_updates=2):

        self.update_kwargs = {
            'the_file': config.path_to_one_file(),
            'configs_directory': config.path_to_projects_configs(),
            'verbose': config.verbose(),
            'full_verbose': True
        }
        self.demonize = demonize
        self.delay_between_updates = delay_between_updates

    def run(self):
        u = Updater(**self.update_kwargs)
        while True:
            u.run()
            if not self.demonize:
                break
            sleep(self.delay_between_updates)



class WebThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        from modules import web_server
        web_server.run()


if __name__ == "__main__":
    args = arguments.parse_args()
    config = ConfigReader('conf/updater.conf')
    logging.basicConfig(
        filename=config.log_file(),
        level=logging.getLevelName(config.log_level().upper()),
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


    updater_kwargs = {}

    if len(sys.argv) > 1:
        # called script with args, so check the args, and override the configs settings
        if args.ini:
            config.set_path_to_one_file(args.ini)
            updater_kwargs['demonize'] = False

        if args.configs_directory:
            config.set_path_to_projects_configs(args.configs_directory)

        config.set_active_web(args.web)

    if config.active_web():
        web_thread = WebThread()
        web_thread.start()

    updater = TheUpdaterDaemon(config, **updater_kwargs)
    updater.run()
