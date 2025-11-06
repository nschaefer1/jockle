import logging 

from backend.base_api import BaseAPI

class APIPut(BaseAPI):
    
    def __init__(self, db_manager):
        self.db_manager = db_manager