import requests
import logging
import json
from src.common import Client

logger = logging.getLogger("catalog")

class Catalog(Client):
    
    def create_catalog(self, name, fields):
        # Construct request
        url = self.url + "/data/v2/projects/{}/catalogs".format(self.project_token)
        payload = {
            "name": name,
            "fields": [ {"name": field } for field in fields ]
        }
        headers = self.basic_auth.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            return response["id"]
        else:
            logger.error(response)
            return False
    
    def get_catalog_name(self, catalog_id):
        # Construct request
        url = self.url + "/data/v2/projects/{}/catalogs/{}".format(self.project_token, catalog_id)
        headers = self.basic_auth.get_headers()
        response = requests.request("GET", url, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            return response["data"]["name"]
        else:
            logger.error(response)
            return None
    
    def get_catalog_items(self, catalog_id, params=None):
        # Construct request
        if bool(params):
            query_string = "?" + urlencode(params)
        else:
            query_string = ""
        url = self.url + "/data/v2/projects/{}/catalogs/{}/items{}".format(self.project_token, catalog_id, query_string)
        headers = self.basic_auth.get_headers()
        response = requests.request("GET", url, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            del response["success"]
            for item in response["data"]:
                del item["catalog_id"]
            return response
        else:
            logger.error(response)
            return None
    
    def update_catalog_name(self, catalog_id, catalog_name, fields):
        # Construct request
        url = self.url + "/data/v2/projects/{}/catalogs/{}".format(self.project_token, catalog_id)
        payload = { "name": catalog_name, "fields": [ { "name": field } for field in fields ] }
        headers = self.basic_auth.get_headers()
        response = requests.request("PUT", url, json=payload, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            return True
        else:
            logger.error(response)
            return False
    
    def create_catalog_item(self, catalog_id, item_id, properties):
        # Construct request
        url = self.url + "/data/v2/projects/{}/catalogs/{}/items/{}".format(self.project_token, catalog_id, item_id)
        payload = { "properties": properties }
        headers = self.basic_auth.get_headers()
        response = requests.request("PUT", url, json=payload, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            return True
        else:
            logger.error(response)
            return False
    
    def update_catalog_item(self, catalog_id, item_id, properties):
        # Construct request
        url = self.url + "/data/v2/projects/{}/catalogs/{}/items/{}/partial-update".format(self.project_token, catalog_id, item_id)
        payload = { "properties": properties }
        headers = self.basic_auth.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            return True
        else:
            logger.error(response)
            return False
    
    def delete_catalog_item(self, catalog_id, item_id):
        # Construct request
        url = self.url + "/data/v2/projects/{}/catalogs/{}/items/{}".format(self.project_token, catalog_id, item_id)
        headers = self.basic_auth.get_headers()
        response = requests.request("DELETE", url, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            return True
        else:
            logger.error(response)
            return False
    
    def delete_catalog_items(self, catalog_id):
        # Construct request
        url = self.url + "/data/v2/projects/{}/catalogs/{}/items".format(self.project_token, catalog_id)
        headers = self.basic_auth.get_headers()
        response = requests.request("DELETE", url, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            return True
        else:
            logger.error(response)
            return False

    def delete_catalog(self, catalog_id):
        # Construct request
        url = self.url + "/data/v2/projects/{}/catalogs/{}".format(self.project_token, catalog_id)
        headers = self.basic_auth.get_headers()
        response = requests.request("DELETE", url, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            return True
        else:
            logger.error(response)
            return False