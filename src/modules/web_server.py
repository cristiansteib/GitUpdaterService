from flask import Flask, abort, request
import logging
from modules.config_reader import ConfigReader
from modules.updater import Updater
import json
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


@app.route('/', methods=['POST', 'GET'])
def index():
    if not request.json:
        abort(400)
    data = request.json
    # todo check json git project name
    updater.run_if_project_exists('unAventon')
    return json.dumps(data)


def run(*args, **kwargs):
    config_instance = ConfigReader('conf/config.ini')
    global updater
    updater = Updater(
        configs_directory=config_instance.configs_directory(),
    )
    app.run(*args, debug=True, host=config_instance.web_host(), port=config_instance.web_port(), **kwargs)

if __name__ == '__main__':
    run()
