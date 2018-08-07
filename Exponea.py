import logging
import sys
from src.common import BasicAuth
from src.analyses import Analyses
from src.catalog import Catalog
from src.customer import Customer
from src.tracking import Tracking

logger = logging.getLogger("exponea")

class Exponea:
    def __init__(self, project_token, username="", password="", url=None):
        self.Analyses = Analyses(project_token, username=username, password=password, url=url)
        self.Catalog = Catalog(project_token, username=username, password=password, url=url)
        self.Customer = Customer(project_token, username=username, password=password, url=url)
        self.Tracking = Tracking(project_token, username=username, password=password, url=url)
    
    def configure(self, project_token=None, username=None, password=None, url=None):
        self.Analyses.configure(project_token=project_token, username=username, password=password, url=url)
        self.Catalog.configure(project_token=project_token, username=username, password=password, url=url)
        self.Customer.configure(project_token=project_token, username=username, password=password, url=url)
        self.Tracking.configure(project_token=project_token, username=username, password=password, url=url)
