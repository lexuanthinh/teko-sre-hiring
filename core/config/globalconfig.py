import yaml

from core.error import *


class GlobalConfig(object):
    __instance = None

    def __init__(self):
        if GlobalConfig.__instance is not None:
            raise InternalError(ERROR_COMMON_0001)

        # Get the configuarion information from yaml file
        configPath = 'core/config/config.yaml'
        cfg = self.__loadConfig(configPath)
        self.LOG_CONFIG = cfg['log_config']
        GlobalConfig.__instance = self

    @staticmethod
    def instance():
        """ Static access method. """
        if GlobalConfig.__instance is None:
            GlobalConfig()
        return GlobalConfig.__instance

    def __loadConfig(self, configPath):
        """
        Get the configuration information from yaml file

        Parameters
        ----------
        configPath : str
            Configuration file path (*.yaml)

        Returns
        -------
        : dict
            The configuration information
        """
        with open(configPath, 'r') as f:
            cfg = yaml.load(f, Loader=yaml.SafeLoader)
        cfg = cfg[cfg['env']]
        return cfg
