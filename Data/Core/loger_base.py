import logging


logger = logging

logger.basicConfig(level= logging.DEBUG,
                   format = "%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
                   datefmt = "%m/%d/%y %I:%M:%S %p",
                   handlers=[
                       logging.FileHandler("Data/errorlog"),
                       logging.StreamHandler()
                   ])
