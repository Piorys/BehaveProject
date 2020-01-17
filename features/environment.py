from src.helpers import Logger
from src.config import TestConf

def before_all(context):
    Logger.start_logger()


def after_all(context):
    Logger.stop_logger()


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    TestConf.driver.close()
