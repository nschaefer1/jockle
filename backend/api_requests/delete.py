import logging 

from backend.base_api import BaseAPI

class APIDelete(BaseAPI):
    
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # TODO add a "PRAGMA foreign_keys = ON;" before we do any deletions to ensure cascading