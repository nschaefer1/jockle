import logging
import sys
import os

from .api_requests import (
    APIGet, 
    APIDelete, 
    APIPatch, 
    APIPost, 
    APIPut
)

#################################################################
# Main API
#################################################################

class API(APIGet, APIDelete, APIPatch, APIPost, APIPut):
    
    def __init__(self, db_manager):
        self.db_manager = db_manager # DB manager instance is passed in
        self.session = {}

    def resolve_path(self, rel_path: str) -> str:
        full = self.app_path(f'../frontend/{rel_path}')
        return full.replace('\\', '/')
    
    def app_path(self, relative_path):
        if getattr(sys, 'frozen', False):   # Checks to see if we're running as an executable
            base_dir = os.path.dirname(sys.executable)
        else:   # This is the dev-env
            base_dir = os.path.dirname(__file__)
        return os.path.join(base_dir, relative_path)