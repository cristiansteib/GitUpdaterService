# -*- coding: utf-8 -*-
"""
    server.py
    ~~~~~~ on December 07,2018 23:47

    This is a web service.

"""


from flask import Flask
import logging


# log
"""
logging.basicConfig(
    filename=CONFIG.LOG_FILE_PATH,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
"""


class WebServer:

    def __init__(self, path_to_git_project_configs=None, host='0.0.0.0', port=8080, endpoint='/'):
        self.port = 8080
        self.host = '0.0.0.0'
        endpoint = '/'
        flask = Flask('web_server_git_updater')


        def run():
            flask.run(debug=False, host=self.host, port=self.port)

        @flask.route(endpoint)
        def listener():
            return "Hello world"

        run()
