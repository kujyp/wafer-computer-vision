import logging



def initLogger():
    logger = logging.getLogger("crumbs")
    logger.setLevel(
        logging.DEBUG)
    streamHandler = logging.StreamHandler()
    logger.addHandler(streamHandler)
    return logger

logger = initLogger()