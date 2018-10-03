class AnalysisType:
    FUNNEL = 'funnel'
    REPORT = 'report'
    SEGMENTATION = 'segmentation'


ANALYSIS_TYPES = {
    AnalysisType.FUNNEL,
    AnalysisType.REPORT,
    AnalysisType.SEGMENTATION,
}


class Analyses:
    def __init__(self, client):
        self.client = client
        self.endpoint_base = '/data/v2/projects/{}/analyses'.format(client.project_token)

    def get_analysis(self, analysis_type, analysis_id):
        """Generic method for getting any type of analyses"""
        assert analysis_type in ANALYSIS_TYPES, 'Unknown analysis type "{}"'.format(analysis_type)
        path = '{}/{}'.format(self.endpoint_base, analysis_type)
        payload = {'analysis_id': analysis_id, 'format': 'table_json'}
        response = self.client.post(path, payload)
        # In case analysis is not found
        if response is None:
            return None
        headers = response['header']
        result = {'name': response['name'], 'data': []}
        for row in response['rows']:
            item = {}
            for index, data in enumerate(row):
                item[headers[index]] = data
            result['data'].append(item)
        return result

    def get_funnel(self, funnel_id):
        return self.get_analysis(AnalysisType.FUNNEL, funnel_id)

    def get_report(self, report_id):
        return self.get_analysis(AnalysisType.REPORT, report_id)

    def get_segmentation(self, segmentation_id):
        return self.get_analysis(AnalysisType.SEGMENTATION, segmentation_id)
