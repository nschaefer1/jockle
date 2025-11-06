import os
import sys
import webview

from .db_manager import DBManager
from backend import API


class MainApp:

    def __init__(self):
        
        # Database control
        self.db_manager = DBManager()
        # API (pass in DB manager here)
        self.api = API(self.db_manager)
        # App entry point
        index_html = self.app_path('../frontend/views/inventory.html').replace('\\','/')

        # Instantiate the window
        self.window = webview.create_window(
            'Window Title',
            f'file:///{index_html}',
            width=1200,
            height=800,
            js_api=self.api
        )

    def app_path(self, relative_path):
        if getattr(sys, 'frozen', False):   # Checks to see if we're running as an executable
            base_dir = os.path.dirname(sys.executable)
        else:   # This is the dev-env
            base_dir = os.path.dirname(__file__)
        return os.path.join(base_dir, relative_path)

    def run(self):
        webview.start(debug=False)


if __name__ == '__main__':
    app = MainApp()
    app.run()