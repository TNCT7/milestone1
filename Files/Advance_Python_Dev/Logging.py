import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]:%(message)s',
    datefmt= '%d-%m-%Y %H-%M-%S',
    level=logging.DEBUG,
    filename='log.txt'
)

logger = logging.getLogger('Test_Log')


logger.info("Informative data")
logger.debug("This is a debug messages")
logger.error("Error has occured")
logger.warning("Warning!!")
