
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
    app = MainApp()
    app.run()