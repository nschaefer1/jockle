import logging 

from backend import BaseAPI

class APIDelete(BaseAPI):
    
    def __init__(self, db_manager):
        self.db_manager = db_manager