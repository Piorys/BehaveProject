from src.config import TestConf
from src.helpers import Logger


def before_all(context):
    Logger.start_logger()


def after_all(context):
    Logger.stop_logger()


def before_scenario(context):
    context.browser = TestConf.driver
    TestConf.driver.get(TestConf.env)


def after_scenario(context):
    TestConf.driver.close()
