import sqlite3 as sql
import logging
import os

from models import DBReturn
from utils import read_basic_file, load_csv

class DBManager:
    
    db_path = 'jockle_db.db'
    
    def __init__(self):
        # Initial DB Setup ran at app startup during class instantiation
        result = self.execute_path(path = 'sql/create_dim.sql', script = True)
        if not result.success:
            raise RuntimeError('Database dimension initialization failed')
        result = self.execute_path(path = 'sql/create_ft.sql', script = True)
        if not result.success:
            raise RuntimeError('Database fact initialization failed')
        # TODO add index creation calls for foriegn keys
            
        self._icon_seeding() # Run icon seeding at the start
        # Only run seeding if we're in dev mode
        if os.getenv('DEBUG') == 'true':
            self._dev_seeding()

    def execute(self, query, params=None):
        '''
        Basic DB execution command with optional parameter inputs
        Any changes are rolled back if any errors are raised
        '''
        with sql.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                if params is not None:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                rows = cursor.fetchall()
                conn.commit()
                columns = tuple([desc[0] for desc in cursor.description]) if cursor.description else ()
                return DBReturn(
                    success = True,
                    columns = columns,
                    rows = rows,
                    row_count = len(rows)
                )
            except Exception as e:
                conn.rollback()
                logging.exception(f'Execution failed, transaction rolled back: {e}')
                # Graceful failing if we are not in debug mode
                if (os.getenv("DEBUG") == 'true'):
                    raise
                else:
                    return DBReturn(
                        success = False
                    )
    
    def execute_script(self, query):
        '''
        Execute an entire SQL script in the database
        This operation does not take parameters
        '''
        with sql.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.executescript(query)
                conn.commit()
                return DBReturn(
                    success = True
                )
            except Exception as e:
                conn.rollback()
                logging.exception(f'SQL Script execution failed, transaction rolled back: {e}')
                # Graceful failing if we are not in debug mode
                if (os.getenv("DEBUG") == 'true'):
                    raise
                else:
                    return DBReturn(
                        success = False
                    )
    
    def execute_path(self, path, script=False, params=None):
        '''
        Read & Execute a given SQL path
        - script=False → normal single-statemnet execute()
        - script=True → multi-statement executescript()
        '''
        query = read_basic_file(path)
        if script:
            return self.execute_script(query)
        else:
            return self.execute(query, params)
        
    def executemany(self, query, param_list):
        '''
        Efficient batch insert/update/delete.
        param_list: list of tuples matching the ? placeholders
        '''
        with sql.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.executemany(query, param_list)
                conn.commit()
                return DBReturn(success=True)
            except Exception as e:
                conn.rollback()
                logging.exception(f'executemany failed: {e}')
                if os.getenv("DEBUG") == 'true':
                    raise
                return DBReturn(success=False)
            
    def _icon_seeding(self):
        '''
        This seeds the icon table specifically to map the icon paths to the dataset
        '''
        # dim_icon seeding
        raw_rows = load_csv('sql/csv_seeds/seed_dim_icon.csv')
        rows = [(
            r['icon_ck'],
            r['icon_path']
        ) for r in raw_rows]
        result = self.executemany(
            'INSERT INTO dim_icon VALUES (?, ?) ON CONFLICT(icon_ck) DO NOTHING;',
            rows
        )
        if not result.success:
            raise RuntimeError('Database dim_icon seeding failed')

    def _dev_seeding(self):
        '''
        Seeding function for development mode
        This should not be ran outside of development
        '''
       

        # dim_inventory seeding
        raw_rows = load_csv('sql/csv_seeds/seed_dim_inventory.csv')
        rows = [(
            r['inv_ck'],
            r['inv_name'],
            r['inv_desc'],
            r['child_ind'],
            r['inv_type'],
            r['equip_location'],
            r['rarity'],
            r['icon_ck']
        ) for r in raw_rows]
        result = self.executemany(
            'INSERT INTO dim_inventory VALUES (?,?,?,?,?,?,?,?) ON CONFLICT(inv_ck) DO NOTHING;',
            rows
        )
        if not result.success:
            raise RuntimeError('Database dim_inventory seeding failed')

        # dim_character seeding
        raw_rows = load_csv('sql/csv_seeds/seed_dim_character.csv')
        rows = [(
            r['char_ck'],
            r['char_name']
        ) for r in raw_rows]
        result = self.executemany(
            'INSERT INTO dim_character (char_ck, char_name) VALUES (?, ?) ON CONFLICT(char_ck) DO NOTHING;',
            rows
        )
        if not result.success:
            raise RuntimeError('Database dim_character seeding failed')
        
        # ft_inventory seeding
        raw_rows = load_csv('sql/csv_seeds/seed_ft_inventory.csv')
        rows = [(
            r['inv_trans_ck'],
            r['inv_ck'],
            r['char_ck'],
            r['val']
        ) for r in raw_rows]
        result = self.executemany(
            'INSERT INTO ft_inventory VALUES (?, ?, ?, ?) ON CONFLICT(inv_trans_ck) DO NOTHING;',
            rows
        )
        if not result.success:
            raise RuntimeError('Database ft_inventory seeding failed')
