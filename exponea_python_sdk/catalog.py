from urllib.parse import urlencode


class Catalog:
    def __init__(self, client):
        self.client = client
        self.endpoint_base = '/data/v2/projects/{}/catalogs'.format(client.project_token)

    def create_catalog(self, name, fields):
        path = self.endpoint_base
        payload = {'name': name, 'fields': [{'name': field} for field in fields]}
        response = self.client.post(path, payload)
        if response is None:
            return None
        return response['id']

    def get_catalog_name(self, catalog_id):
        path = '{}/{}'.format(self.endpoint_base, catalog_id)
        response = self.client.get(path)
        if response is None:
            return None
        return response['data']['name']

    def get_catalog_items(self, catalog_id, params=None):
        # URL encode any filters and params
        query_string = '?{}'.format(urlencode(params)) if params else ''
        path = '{}/{}/items{}'.format(self.endpoint_base, catalog_id, query_string)
        response = self.client.get(path)
        if response is None:
            return None
        # Delete unnecessary attributes
        del response['success']
        for item in response['data']:
            del item['catalog_id']
        return response

    def update_catalog_name(self, catalog_id, catalog_name, fields):
        path = '{}/{}'.format(self.endpoint_base, catalog_id)
        payload = {'name': catalog_name, 'fields': [{'name': field} for field in fields]}
        response = self.client.put(path, payload)
        if response is None:
            return None
        return response['success']

    def create_catalog_item(self, catalog_id, item_id, properties):
        path = '{}/{}/items/{}'.format(self.endpoint_base, catalog_id, item_id)
        payload = {'properties': properties}
        response = self.client.put(path, payload)
        return None if response is None else response['success']

    def update_catalog_item(self, catalog_id, item_id, properties):
        path = '{}/{}/items/{}/partial-update'.format(self.endpoint_base, catalog_id, item_id)
        payload = {'properties': properties}
        response = self.client.post(path, payload)
        return None if response is None else response['success']

    def delete_catalog_item(self, catalog_id, item_id):
        path = '{}/{}/items/{}'.format(self.endpoint_base, catalog_id, item_id)
        response = self.client.delete(path)
        return None if response is None else response['success']

    def delete_catalog_items(self, catalog_id):
        path = '{}/{}/items'.format(self.endpoint_base, catalog_id)
        response = self.client.delete(path)
        return None if response is None else response['success']

    def delete_catalog(self, catalog_id):
        path = '{}/{}'.format(self.endpoint_base, catalog_id)
        response = self.client.delete(path)
        return None if response is None else response['success']
