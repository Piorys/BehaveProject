import pathlib
import os

from src.config import TestConf
from datetime import datetime

screenshot_dir = str(pathlib.Path(__file__).parent.absolute()) + '/../../' + TestConf.screenshot_dir + '/'


def clear_screenshot_dir():
    if os.path.exists(screenshot_dir):
        os.removedirs(screenshot_dir)


def generate_file_name():
    return datetime.now().strftime('%Y%m%d%H%M%S') + '.png'


def make_screenshot(driver):
    driver.save_screenshot(generate_file_name())
