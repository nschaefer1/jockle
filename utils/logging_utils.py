import logging


######################################################################
# Logging Startups
######################################################################

# This is a console logger
def init_basic_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )

# This is a console and file logger
def init_logger(log_file, set_mode='a'):
    if set_mode not in ('w', 'a'):
        raise ValueError("Invalid mode: set_mode must be 'w' (write) or 'a' (append).")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file, mode=set_mode)
        ]
    )