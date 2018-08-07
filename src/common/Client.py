import logging
from src.common.BasicAuth import BasicAuth

URL_DEFAULT = "https://api.exponea.com"

logger = logging.getLogger("client")

class Client:
    def __init__(self, project_token, username="", password="", url=None, logger=None):
        self.project_token = project_token
        self.basic_auth = BasicAuth(username, password)
        self.url = url or URL_DEFAULT
        self.logger = logger or logging.getLogger()
    
    def configure(self, project_token=None, username=None, password=None, url=None):
        if project_token is not None:
            self.project_token = project_token
        if username is not None and password is not None:
            self.basic_auth = BasicAuth(username, password)
        if url is not None:
            self.url = url
    
    def catch_error_response(self, response):
        if response.status_code == 401:
            logger.error("401: Unauthorized request.")
            raise Exception("Unauthorized request.")
        elif response.status_code == 404:
            logger.error("404: Object does not exist.")
            return None
