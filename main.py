
from dotenv import load_dotenv
import os

from managers import (
    MainApp
)

from utils import (
    init_basic_logger
)

#################################################################
# App Entry point
#################################################################

if __name__ == '__main__':
    init_basic_logger()
    load_dotenv()           # Loading environment variables if any
    app = MainApp()
    app.run()