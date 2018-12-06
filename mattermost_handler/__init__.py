# coding=utf-8

name = "mattermost_handler"

import logging
import requests

logger = logging.getLogger(__name__)


class MattermostIncomeWebhookHandler(logging.Handler):
    def __init__(self, url):
        super(MattermostIncomeWebhookHandler, self).__init__()
        self.url = url

        if self.url is None:
            logger.warning("Mattermost webhook url cannot be None")

    def emit(self, record):
        if self.url is not None:
            requests.post(self.url, json={"text": self.format(record)})
