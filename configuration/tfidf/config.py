import logging

from singleton_decorator import singleton
import yaml

logger = logging.getLogger(__name__)

class InvalidConfigException(Exception):
    pass


@singleton
class TfidfConfig(object):
    def __init__(self, profile):
        self.profile = profile
        self.current_config = None

    def get_current_config(self):
        cfg = None
        with open("configuration/tfidf/config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

        if cfg is not None:
            logger.info("Succesfully loaded configuration")
            return cfg[self.profile]

        if self.current_config is not None:
            logger.warning("Failed to load new configuration. returning last valid lda")
            return self.current_config
        else:
            raise InvalidConfigException("Could not load new lda. No existing lda available either")
