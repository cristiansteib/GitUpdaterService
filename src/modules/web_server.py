from flask import Flask, abort, request
import logging
from modules.config_reader import ConfigReader
from modules.updater import Updater
import json

app = Flask(
    'WebGitUpdaterService',
)
config_instance = ConfigReader('conf/updater.conf')

# global instance for Updater class
updater = None

# log

logging.basicConfig(
    filename=config_instance.log_file(),
    level=logging.getLevelName(config_instance.log_level().upper()),
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def github_get_repo_name(data):
    return data['repository']['name']


def gitlab_get_repo_name(data):
    pass


def gogs_get_repo_name(data):
    pass


def isGithub(data):
    pass


def isGitlab(data):
    pass


def isGogs(data):
    pass


def get_repo_name(data):
    if isGithub(data):
        return github_get_repo_name(data)
    elif isGitlab(data):
        return gitlab_get_repo_name(data)
    elif isGogs(data):
        return gogs_get_repo_name(data)


@app.route(config_instance.url_path(), methods=['POST', 'GET'])
def index():
    print('Request webHook')
    if not request.json:
        abort(400)
    data = request.json
    repo_name = get_repo_name(data)
    updater.run_if_project_exists(repo_name)
    return json.dumps(data)


def run():
    global updater
    updater = Updater(
        configs_directory=config_instance.path_to_projects_configs(),
    )
    app.run(debug=False, host=config_instance.web_host(), port=config_instance.web_port())


if __name__ == '__main__':
    run()
