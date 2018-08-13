class Catalog:
    def __init__(self, client):
        self.client = client
        self.endpoint_base = "/data/v2/projects/{}/catalogs".format(client.project_token)
    
    def create_catalog(self, name, fields):
        path = self.endpoint_base
        payload = { "name": name, "fields": [ {"name": field } for field in fields ] }
        response = self.client.request("POST", path, payload)
        if response is None:
            return None
        return response["id"]
            
    def get_catalog_name(self, catalog_id):
        path = self.endpoint_base + "/{}".format(catalog_id)
        response = self.client.request("GET", path)
        if response is None:
            return None
        return response["data"]["name"]            
    
    def get_catalog_items(self, catalog_id, params=None):
        # URL encode any filters and params
        if bool(params):
            query_string = "?" + urlencode(params)
        else:
            query_string = ""
        path = self.endpoint_base + "/{}/items{}".format(catalog_id, query_string)
        response = self.client.request("GET", path)
        if response is None:
            return None
        # Delete unnecessary attributes
        del response["success"]
        for item in response["data"]:
            del item["catalog_id"]
        return response
    
    def update_catalog_name(self, catalog_id, catalog_name, fields):
        path = self.endpoint_base + "/{}".format(catalog_id)
        payload = { "name": catalog_name, "fields": [ { "name": field } for field in fields ] }
        response = self.client.request("PUT", path, payload)
        if response is None:
            return None
        return response["success"]
    
    def create_catalog_item(self, catalog_id, item_id, properties):
        path = self.endpoint_base + "/{}/items/{}".format(catalog_id, item_id)
        payload = { "properties": properties }
        response = self.client.request("PUT", path, payload)
        if response is None:
            return None
        return response["success"]
    
    def update_catalog_item(self, catalog_id, item_id, properties):
        path = self.endpoint_base + "/{}/items/{}/partial-update".format(catalog_id, item_id)
        payload = { "properties": properties }
        response = self.client.request("POST", path, payload)
        if response is None:
            return None
        return response["success"]
    
    def delete_catalog_item(self, catalog_id, item_id):
        path = self.endpoint_base + "/{}/items/{}".format(catalog_id, item_id)
        response = self.client.request("DELETE", path)
        if response is None:
            return None
        return response["success"]
    
    def delete_catalog_items(self, catalog_id):
        path = self.endpoint_base + "/{}/items".format(catalog_id)
        response = self.client.request("DELETE", path)
        if response is None:
            return None
        return response["success"]

    def delete_catalog(self, catalog_id):
        path = self.endpoint_base + "/{}".format(catalog_id)
        response = self.client.request("DELETE", path)
        if response is None:
            return None
        return response["success"]