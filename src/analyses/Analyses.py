import requests
import json
from src.common import Client

class Analyses(Client):
    
    def get_funnel(self, funnel_id):
        # Construct request
        url = self.url + "/data/v2/projects/{}/analyses/funnel".format(self.project_token)
        payload = {
            "analysis_id": funnel_id,
            "format": "table_json"
        }
        headers = self.basic_auth.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            headers = response["header"]
            result = { "name": response["name"], "data": [] }
            for row in response["rows"]:
                drill_down_row = {}
                for index, data in enumerate(row):
                    drill_down_row[headers[index]] = data
                result["data"].append(drill_down_row)
            return result
        return None
    
    def get_report(self, report_id):
        # Construct request
        url = self.url + "/data/v2/projects/{}/analyses/report".format(self.project_token)
        payload = {
            "analysis_id": report_id,
            "format": "table_json"
        }
        headers = self.basic_auth.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            headers = response["header"]
            result = { "name": response["name"], "data": [] }
            for row in response["rows"]:
                data_row = {}
                for index, data in enumerate(row):
                    data_row[headers[index]] = data
                result["data"].append(data_row)
            return result
        return None
    
    def get_segmentation(self, segmentation_id):
        # Construct request
        url = self.url + "/data/v2/projects/{}/analyses/segmentation".format(self.project_token)
        payload = {
            "analysis_id": segmentation_id,
            "format": "table_json"
        }
        headers = self.basic_auth.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            headers = response["header"]
            result = { "name": response["name"], "data": [] }
            for row in response["rows"]:
                data_row = {}
                for index, data in enumerate(row):
                    data_row[headers[index]] = data
                result["data"].append(data_row)
            return result
        return None
