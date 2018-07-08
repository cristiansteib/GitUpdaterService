from flask import Flask
import logging
from modules.config_reader import ConfigReader
from modules.updater import Updater

app = Flask(
    'WebGitUpdaterService',
)

updater = None
# log
logging.basicConfig(
    filename='log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


@app.route('/')
def index():
    updater.run_if_project_exists('unAventon')
    return 'Hello world'


def run(*args, **kwargs):
    config_instance = ConfigReader()
    global updater
    updater = Updater(
        configs_directory=config_instance.configs_directory(),
    )
    app.run(*args, debug=False, host=config_instance.web_host(), port=config_instance.web_port(), **kwargs)

if __name__ == '__main__':
    run()
