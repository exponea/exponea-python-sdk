class Analyses:
    def __init__(self, client):
        self.client = client
        self.endpoint_base = "/data/v2/projects/{}/analyses".format(client.project_token)
    
    # Generic method for getting any type of Analyses
    def get_analysis(self, analysis_type, analysis_id):
        # Construct request
        path = self.endpoint_base + "/" + analysis_type
        payload = { "analysis_id": analysis_id, "format": "table_json" }
        response = self.client.request("POST", path, payload)
        # In case analysis is not found
        if response is None:
            return None
        headers = response["header"]
        result = { "name": response["name"], "data": [] }
        for row in response["rows"]:
            item = {}
            for index, data in enumerate(row):
                item[headers[index]] = data
            result["data"].append(item)
        return result
    
    def get_funnel(self, funnel_id):
        return self.get_analysis("funnel", funnel_id)
    
    def get_report(self, report_id):
        return self.get_analysis("report", report_id)
    
    def get_segmentation(self, segmentation_id):
        return self.get_analysis("segmentation", segmentation_id)
