Описание
-----------
Менеджер для работы с ArgoCD

Установка пакетом
-----------
Для локальной разработки::
    pip install -e packages/simple_logger
Для обычной установки через requirements.txt::
    simple_logger @ git+https://github.com/dkramorov/simple_logger.git


Импорт
-----------
Проверка::
    from managers.simple_logger import logger


Удаление
-----------
Удалить пакет::
    pip uninstall simple_logger

Для создания пакета
https://docs.python.org/3.10/distutils/introduction.html#distutils-simple-example
https://docs.python.org/3.10/distutils/sourcedist.html
::
    python setup.py sdist




