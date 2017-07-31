# coding=utf-8

import logging
import requests


class MattermostIncomeWebhookHandler(logging.Handler):
    def __init__(self, url):
        super(MattermostIncomeWebhookHandler, self).__init__()
        self.url = url

    def emit(self, record):
        requests.post(self.url, json={"text": self.format(record)})
