import logging 

from backend.base_api import BaseAPI
from models import APIResponse

class APIGet(BaseAPI):
    
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def getInventory(self, char_ck):
        '''
        Get the inventory for a specific char_ck given
        char_ck: unique identifier in the DB
        '''
        db_result = self.db_manager.execute_path('sql/inventory/char_inventory.sql', params=(char_ck,))
        if not db_result.success:
            logging.exception('API GET Error: db_return return was unsuccessful')
            return APIResponse(success = False, message = 'API unable to pull from database').to_dict()
        
        logging.info('API GET: getInventory successful')
        return APIResponse(
            success = True,
            data = self._pull_into_json(db_result.rows, db_result.columns)
        ).to_dict()

        