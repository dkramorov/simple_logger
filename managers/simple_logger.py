import logging


def create_logger(log_format: str = '%(asctime)s %(message)s'):
    """Простой логгер для отладки
       %(pathname)s Full pathname of the source file where the logging call was issued (if available)
       %(filename)s Filename portion of pathname.
       %(module)s Module (name portion of filename).
       %(funcName)s Name of function containing the logging call.
       %(lineno)d Source line number where the logging call was issued (if available).
    """
    #log_format = '%(asctime)s [%(filename)s]:[%(funcName)s]:[%(lineno)s] %(message)s'
    logging.basicConfig(format=log_format)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    #logger.info(__file__)
    return logger


def show_all_loggers():
    """Показывает все логгеры
       logger.setLevel(logging.INFO)
    """
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    return loggers


logger = create_logger()
