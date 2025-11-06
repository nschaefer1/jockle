import logging


#################################################################
# Base API Class inhereted by all other classes
#################################################################

class BaseAPI:

    def __init__(self):
        pass

    def _pull_into_json(self, data, col_names):
        return [dict(zip(col_names, row)) for row in data]
    
    def _normalize(self, value):
        if isinstance(value, str) and value.strip() == "":
            return None
        return value
    
    # Session state controls for the app
    def set_session(self, key, value):
        self.session[key] = value
        logging.info(f'Set {key}: {value}')
        return True
    def get_session(self, key):
        return self.session.get(key, None)
    def remove_session(self, key):
        logging.info(f'Removed `{key}` from session')
        return self.session.pop(key, False)