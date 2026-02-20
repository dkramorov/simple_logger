import json
import logging


def json_pretty_print(json_obj, pass_fields: list = None, default_deserializator=str):
    """Вывести json в человеческом виде,
       например,
         json.dumps({'test': 2.34}, default_deserializator=str)
         - если встречается неизвестный тип, будет вызван default_deserializator сериализатор
       :param json_obj: джисонина
       :param pass_fields: пропустить поля (верхний уровень словаря пока)
       :param default_deserializator: функция вызываемая при Object of type X is not JSON serializable
    """
    if pass_fields and isinstance(json_obj, dict):
        new_json_obj = {k: v for k, v in json_obj.copy().items() if not k in pass_fields}
        return json.dumps(new_json_obj, sort_keys=True, indent=2,
                          separators=(',', ': '), ensure_ascii=False, default=default_deserializator)
    return json.dumps(json_obj, sort_keys=True, indent=2,
                      separators=(',', ': '), ensure_ascii=False, default=default_deserializator)


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
