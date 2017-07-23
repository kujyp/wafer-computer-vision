import logging

from utils.base.singleton import Singleton


class Logger(Singleton):
    @classmethod
    def getLogger(cls, log_level):
        logger = cls.getInstance().logger
        if log_level is "DEBUG":
            logger.setLevel(logging.DEBUG)
        elif log_level is "INFO":
            logger.setLevel(logging.INFO)
        return logger

    def __init__(self):
        self.logger = logging.getLogger("JYP")
        self.formatter = \
            logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] '
                              '%(asctime)s > %(message)s')
        self.streamHandler = logging.StreamHandler()
        self.streamHandler.setFormatter(self.formatter)

        self.logger.addHandler(self.streamHandler)

logger = Logger.getLogger("DEBUG")