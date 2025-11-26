import sqlite3 as sql
import logging
import os

from models import DBReturn
from utils import read_basic_file

class DBManager:
    
    db_path = 'jockle_db.db'
    
    def __init__(self):
        # Initial DB Setup ran at app startup during class instantiation
        result = self.execute_path(path = 'sql/create_dim.sql', script = True)
        if not result.success:
            raise RuntimeError('Database initialization failed')

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

