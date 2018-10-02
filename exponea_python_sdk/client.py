import json
import logging

import requests
from requests.auth import HTTPBasicAuth

from exponea_python_sdk.analyses import Analyses
from exponea_python_sdk.catalog import Catalog
from exponea_python_sdk.customer import Customer
from exponea_python_sdk.exceptions import APIException
from exponea_python_sdk.tracking import Tracking

DEFAULT_URL = 'https://api.exponea.com'

logging.basicConfig()
DEFAULT_LOGGER = logging.getLogger('exponea-python-sdk')


class Exponea:
    def __init__(self, project_token, username='', password='', url=None):
        self.project_token = project_token
        self.username = username
        self.password = password
        self.url = url or DEFAULT_URL
        self.logger = DEFAULT_LOGGER
        self.analyses = Analyses(self)
        self.catalog = Catalog(self)
        self.customer = Customer(self)
        self.tracking = Tracking(self)

    def configure(self, project_token=None, username=None, password=None, url=None):
        if project_token is not None:
            self.project_token = project_token
        if username is not None:
            self.username = project_token
        if password is not None:
            self.password = password
        if url is not None:
            self.url = url
        return self

    def request(self, method, path, payload=None):
        url = self.url + path
        self.logger.debug('Sending %s request to %s', method, url)
        response = requests.request(method, url, json=payload, auth=HTTPBasicAuth(self.username, self.password))
        status = response.status_code
        self.logger.debug('Response status code: %d', status)
        result = json.loads(response.text)
        if status == 200 and result['success']:
            return result
        self.logger.error(response.text)
        if result.get('error') is not None:
            raise APIException(result['error'])
        elif result.get('errors'):
            errors = result['errors']
            if type(errors) == list:
                raise APIException(result['errors'])
            elif type(errors) == dict:
                raise APIException(list(result['errors'].values()))
        raise APIException(response.text)

    def get(self, path):
        return self.request('GET', path)

    def post(self, path, payload=None):
        return self.request('POST', path, payload)

    def delete(self, path, payload=None):
        return self.request('DELETE', path, payload)

    def put(self, path, payload=None):
        return self.request('PUT', path, payload)
