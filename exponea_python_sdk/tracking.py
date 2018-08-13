class Tracking:
    def __init__(self, client):
        self.client = client
        self.endpoint_base = "/track/v2/projects/{}".format(client.project_token)

    def get_system_time(self, batch=False):
        if batch:
            return { "name": "system/time" }
        path = self.endpoint_base + "/system/time"
        response = self.client.request("GET", path)
        if response is None:
            return None
        return response["time"]
    
    def update_customer_properties(self, customer_ids, properties, batch=False):
        if batch:
            return { "name": "customers", "data": { "customer_ids": customer_ids, "properties": properties } }
        path = self.endpoint_base + "/customers"
        payload = { "customer_ids": customer_ids, "properties": properties }
        response = self.client.request("POST", path, payload)
        if response is None:
            return None
        return response["success"]
    
    def add_event(self, customer_ids, event_type, properties=None, timestamp=None, batch=False):
        payload = { "customer_ids": customer_ids, "timestamp": timestamp, "properties": properties, "event_type": event_type }
        if batch:
            return { "name": "customers/events", "data": payload }
        path = self.endpoint_base + "/customers/events"
        response = self.client.request("POST", path, payload)
        if response is None:
            return None
        return response["success"]
    
    def batch_commands(self, commands):
        path = self.endpoint_base + "/batch"
        payload = { "commands": commands }
        response = self.client.request("POST", path, payload)
        if response is None:
            return None
        result = []
        for res in response["results"]:
            if res.get("time"):
                result.append(res["time"])
            else:
                result.append(res["success"])
        return result
