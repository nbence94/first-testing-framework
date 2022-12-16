import logging


class Logger:

    @staticmethod
    def log_info():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename=r'.\Logs\mylog.log', mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger


