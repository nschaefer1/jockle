import logging 
import base64
from pathlib import Path

from backend.base_api import BaseAPI
from models import APIResponse

class APIPost(BaseAPI):
    
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def receive_png_base64(self, filename, base64_data):
        '''
        Receive a PNG in base64 format
    
        Parameters
        -----
        filename : str
            File name with .png extension
            
        base64_data : base64 PNG Object
            Actual base64 data object expected to be received from a JS API POST call

        Returns
        -----
        APIResponse Class Variable
        '''
        try:
            save_path = Path(f'frontend/assets/icons/custom/{filename}')
            png_bytes = base64.b64decode(base64_data)
            # Write file
            with open(save_path, 'wb') as f:
                f.write(png_bytes)
            
            return APIResponse(success=True).to_dict()
        except Exception as e:
            return APIResponse(
                success=False,
                message=f'API PNG Post failed: {e}'
            ).to_dict()
        