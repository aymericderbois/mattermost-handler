# coding=utf-8

import logging
import requests

URL = None


class MattermostHandler(logging.Handler):
    def __init__(self):
        if URL is None:
            raise Exception('MattermostHandler: you need to define mattermost_handler.URL with your income url')
        super(MattermostHandler, self).__init__()

    def emit(self, record):
        requests.post(URL, json={"text": self.format(record)})
