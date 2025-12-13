import logging 
import math

from backend.base_api import BaseAPI
from models import APIResponse
from utils import read_json

class APIPatch(BaseAPI):

    scc_path = 'data/static_carry_cap.json'
    
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _calculate_band(self, strength, size, band, quad_bool):
        '''
        Calculate the designated band column for the dim_character table
        
        strength : int
            The strength of the character
        size : str
            The size of the given character
        band : str
            This is the associated band required for the calculation: light, medium, heavy
        '''
        # Read the JSON config file
        json_stats = read_json(self.scc_path)
        # Handle if Strength is < 10
        if strength < 10:
            calc = json_stats['below_nine_strength'][band][strength-1]
        # Handle if Strength is > 10
        else:
            d = strength - 10
            k = math.floor(d / 5)
            r = d % 5
            m_r = json_stats['r_m_multiplier'][r]
            heavy_s = math.floor(100 * (2 ** k) * m_r)

            # Apply side alterations
            if band == 'medium':
                calc = math.floor((2 * heavy_s)/3)
            elif band == 'light':
                calc = math.floor(heavy_s / 3)
            else:
                calc = heavy_s
        # Apply size-scaling
        if quad_bool:
            # If the character has more than 3 legs, than do this
            scalar = json_stats['quad_size_scaling'][size]
        else:
            scalar = json_stats['size_scaling'][size]
        return math.floor(calc * scalar)

    def update_character_carry_bands(self, char_ck): 
        '''
        Update the carry bands in the dim_character table

        char_ck : int
            The unique identifier for the character we want to update
        '''
        # Grab the record of the char_ck from the database
        db_result = self.db_manager.execute(
            'select * from dim_character where char_ck = ?;',
            (char_ck,)
        )
        if not db_result.success:
            logging.exception(f'Could not retrieve character record {char_ck} from database')
            return APIResponse(success = False, message = f'Could not retrieve character record {char_ck} from database').to_dict()
        logging.info(f'Character record {char_ck} retrieved from database')
        
        # Access the strength and size variable
        str_index = db_result.columns.index("str_score")
        size_index = db_result.columns.index("size_cat")
        leg_count = db_result.columns.index("leg_count")
        str_score = db_result.rows[0][str_index]
        size_cat = db_result.rows[0][size_index]
        quad_bool = db_result.rows[0][leg_count] > 3

        # Calculate each individual band based on the strength and size of the candidate
        light_band = self._calculate_band(str_score, size_cat, 'light', quad_bool)
        medium_band = self._calculate_band(str_score, size_cat, 'medium', quad_bool)
        heavy_band = self._calculate_band(str_score, size_cat, 'heavy', quad_bool)

        # Update the designated record and return a success result
        db_result = self.db_manager.execute(
            'update dim_character set light_band = ?, medium_band = ?, heavy_band = ? where char_ck = ?;',
            (light_band, medium_band, heavy_band, char_ck)
        )
        if not db_result.success:
            logging.exception(f'Could not update record {char_ck} with updated stats')
            return APIResponse(success=False, message=f'Could not update record {char_ck} with updated stats')
        logging.info(f'Character {char_ck} updated with light, medium, and heavy bands of {light_band}, {medium_band}, {heavy_band}, respectively.')
        return APIResponse(success = True)
    
    def update_all_carry_bands(self):
        '''
        Update all characters stats at once
        '''
        db_result = self.db_manager.execute(
            'select char_ck from dim_character;'
        )
        if not db_result.success:
            logging.exception(f'Could not pull all char_ck from database')
            return APIResponse(success=False, message=f'Could not pull all char_ck from database')
        logging.info('All char_ck successfully retrieved from database')

        char_ck_list = [r[0] for r in db_result.rows]
        for char_ck in char_ck_list:
            self.update_character_carry_bands(char_ck)
        logging.info('All characters were overriden with automatic carry_band calculations')


