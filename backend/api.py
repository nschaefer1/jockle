import sqlite3 as sql
import logging

from backend import (
    BaseAPI
)
from api_requests import (
    APIGet, 
    APIDelete, 
    APIPatch, 
    APIPost, 
    APIPut
)

#################################################################
# Main API
#################################################################

class API(BaseAPI, APIGet, APIDelete, APIPatch, APIPost, APIPut):
    
    def __init__(self, db_manager):
        self.db_manager = db_manager # DB manager instance is passed in
        self.session = {}

    
    

    