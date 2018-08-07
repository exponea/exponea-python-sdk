import requests
import logging
import json
from src.common import Client

logger = logging.getLogger("customer")

class Customer(Client):
    
    def get_customer(self, ids):
        url = self.url + "/data/v2/projects/{}/customers/export-one".format(self.project_token)
        payload = { "customer_ids": ids }
        headers = self.basic_auth.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            logger.debug("Request successful.")
            return {
                "ids": response["ids"],
                "properties": response["properties"],
                "events": response["events"]
            }
        else:
            logger.error(response)
        return None
    
    def get_customer_consents(self, ids, consents):
        url = self.url + "/data/v2/projects/{}/customers/attributes".format(self.project_token)
        payload = { "customer_ids": ids, "attributes": [{"type": "consent", "category": consent_type} for consent_type in consents]}
        headers = self.basic_auth.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            result = {}
            for index, consent_type in enumerate(consents):
                # Check if user has permission to request data_type
                if not response["results"][index]["success"]:
                    logger.warning("No permission to retrieve consent {}".format(consent_type))
                    result[consent_type] = None
                    continue
                result[consent_type] = response["results"][index]["value"]
            return result
        else:
            logger.error(response)
        return None
    
    def get_customer_attributes(self, customer_ids, properties=[], segmentations=[], ids=[], expressions=[], aggregations=[], predictions=[]):
        # Construct request
        url = self.url + "/data/v2/projects/{}/customers/attributes".format(self.project_token)
        payload = {
            "customer_ids": customer_ids,
            "attributes": 
                [{"type": "property", "property": customer_property} for customer_property in properties] +
                [{"type": "segmentation", "id": segmentation} for segmentation in segmentations] +
                [{"type": "id", "id": id} for id in ids] +
                [{"type": "expression", "id": expression} for expression in expressions] +
                [{"type": "aggregate", "id": aggregate} for aggregate in aggregations] +
                [{"type": "prediction", "id": prediction} for prediction in predictions]
        }
        headers = self.basic_auth.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            result = {}
            data_points = 0
            for data_type in [("properties", properties), ("segmentations", segmentations), ("ids", ids), ("expressions", expressions), ("aggregations", aggregations), ("predictions", predictions)]:
                data_type_name = data_type[0]
                data_type_ids = data_type[1]
                if len(data_type_ids) == 0:
                    continue
                result[data_type_name] = {}
                for id in data_type_ids:
                    # Check if user has permission to request data_type
                    if not response["results"][data_points]["success"]:
                        logger.warning("No permission to retrieve {} {}".format(data_type_name, id))
                        result[data_type_name][id] = None
                        continue
                    result[data_type_name][id] = response["results"][data_points]["value"]
                    data_points += 1
            return result
        else:
            logger.error(response)
        return None
    
    def get_customers(self):
        # Construct request
        url = self.url + "/data/v2/projects/{}/customers/export".format(self.project_token)
        payload = {
            "format": "native_json"
        }
        headers = self.basic_auth.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            logger.debug("Request successful.")
            users = []
            ids = [ field["id"] for field in filter(lambda x: x["type"] == "id" ,response["fields"])]
            properties = [ field["property"] for field in filter(lambda x: x["type"] == "property" ,response["fields"])]
            for row in response["data"]:
                user = { "ids": {}, "properties": {} }
                for index, attribute in enumerate(row):
                    if index < len(ids):
                        user["ids"][ids[index]] = attribute
                    else:
                        user["properties"][properties[index - len(ids)]] = attribute
                users.append(user)
            return users
        else:
            logger.error(response)
        return None
    
    def get_events(self, customer_ids, event_types):
        # Construct request
        url = self.url + "/data/v2/projects/{}/customers/events".format(self.project_token)
        payload = {
            "customer_ids": customer_ids,
            "event_types": event_types
        }
        headers = self.basic_auth.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)
        self.catch_error_response(response)
        # Process response
        response = json.loads(response.text)
        if response["success"]:
            return response["data"]
        else:
            logger.error(response)
        return None
    
    def anonymize_customer(self, customer_ids):
        # Construct request
        url = self.url + "/data/v2/projects/{}/customers/anonymize".format(self.project_token)
        payload = { "customer_ids": customer_ids }
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
