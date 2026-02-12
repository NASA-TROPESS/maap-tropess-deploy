import os
import logging

from dotenv import load_dotenv

from maap.maap import MAAP

logger = logging.getLogger()
class MaapTool(object):

    def __init__(self, env_config_file=None, **kwargs):

        # Load environment variables from a .env file
        load_dotenv(dotenv_path=env_config_file)

        self.maap = MAAP()