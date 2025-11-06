import sqlite3 as sql
import logging

from models import DBReturn


class DBManager:
    
    db_path = 'sqlite_db.db'
    
    def __init__(self):
        conn = sql.connect(self.db_path)
        cursor = conn.cursor()
        try:
            # Database structure
            pass
        except Exception as e:
            conn.rollback()
            logging.exception('Database class cannot be instantiated, transaction rolled back: {e}')
            conn.close()
            raise

    def execute(self, query, params=None):
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
                    columns = columns,
                    rows = rows,
                    row_count = len(rows)
                )
            except Exception as e:
                conn.rollback()
                logging.exception('Execution failed, transaction rolled back: {e}')
                raise
