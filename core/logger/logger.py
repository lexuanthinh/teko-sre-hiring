import logging
from logging.handlers import TimedRotatingFileHandler

from core.config import GlobalConfig
from core.error import *


class Logger(object):
    __instance = None

    def __init__(self):
        if Logger.__instance is not None:
            raise InternalError(ERROR_COMMON_0001)

        logConfig = GlobalConfig.instance().LOG_CONFIG
        file_name = logConfig['file_name'] if 'file_name' in logConfig else 'log_file.log'
        when = logConfig['when'] if 'when' in logConfig else 'midnight'
        interval = int(logConfig['interval']) if 'interval' in logConfig else 1
        backup_count = int(logConfig['backup_count']) if 'backup_count' in logConfig else 7

        # Split log at 0h everyday
        handler = TimedRotatingFileHandler(f'./logs/{file_name}',
                                           when=when,
                                           interval=interval,
                                           backupCount=backup_count)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.__logger = logging.getLogger('RotatingFileHandler')
        self.__logger.setLevel(logging.DEBUG)
        self.__logger.addHandler(handler)
        Logger.__instance = self

    @staticmethod
    def instance():
        """ Static access method. """
        if Logger.__instance is None:
            Logger()
        return Logger.__instance

    def debug(self, content):
        self.__logger.debug(content)

    def info(self, content):
        self.__logger.info(content)

    def warning(self, content):
        self.__logger.warning(content)

    def error(self, content):
        self.__logger.error(content)

    def critical(self, content):
        self.__logger.critical(content)
