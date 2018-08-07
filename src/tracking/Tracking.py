import requests
import json
from src.common import Client

class Tracking(Client):

    def get_system_time(self):
        # Construct request
        url = self.url + "/track/v2/projects/{}/system/time".format(self.project_token)
        headers = self.basic_auth.get_headers()
        response = requests.request("GET", url, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            return response["time"]
        else:
            logger.error(response)
            return False
    
    def update_customer_properties(self, customer_ids, properties):
        # Construct request
        url = self.url + "/track/v2/projects/{}/customers".format(self.project_token)
        payload = {
            "customer_ids": customer_ids,
            "properties": properties
        }
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
    
    def add_event(self, customer_ids, event_type, properties=None, timestamp=None):
        # Construct request
        url = self.url + "/track/v2/projects/{}/customers/events".format(self.project_token)
        payload = {
            "customer_ids": customer_ids,
            "timestamp": timestamp,
            "properties": properties
        }
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
    
    def batch_commands(self, commands):
        # Construct request
        url = self.url + "/track/v2/projects/{}/batch".format(self.project_token)
        payload = { "commands": commands }
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