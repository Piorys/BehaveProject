import os
import pathlib

from src.config import TestConf
from src.helpers import Timestamp as time

root = str(pathlib.Path(__file__).parent.absolute())+'/../../'


def create_output_dir(output_dir):
    """
    Creates directory for output
    :param output_dir: - directory name with path from root folder
    """
    print(time.now() + 'Creating logger directory')
    if not os.path.exists(root + output_dir):
        print(time.now() + 'Logger directory not found, creating')
        os.mkdir(root + output_dir)
    else:
        print(time.now() + 'Logger directory already created')


def clear_logger_file(output_dir, logger_filename):
    """
    Clears content of logger file
    :param output_dir: directory name with path from root folder
    :param logger_filename: name of the logger file
    """
    print(time.now() + 'Clearing logger file contents')
    with open(output_dir + logger_filename, 'w+'):
        pass


def create_logger_file(output_dir, logger_filename):
    """
    Creates logger file
    :param output_dir:
    :param logger_filename: name of the logger file
    """
    print(time.now() + 'Creating logger file')
    if not os.path.exists(root + output_dir + logger_filename):
        print(time.now() + 'Logger file not found, creating')
        open(root + output_dir + logger_filename, 'w')
    else:
        print(time.now() + 'Logger file already created')
        clear_logger_file(root + output_dir, logger_filename)


def start_logger(output_dir=TestConf.output_dir, logger_filename=TestConf.logger_file_name):
    """
    Creates log file which is to be used for logging
    :param output_dir: - Name of directory where output should be stored
    :param logger_filename: name of the logger file
    """
    print('#' * 20)
    print('Starting logger...')
    print('#' * 20)
    create_output_dir(output_dir)
    create_logger_file(output_dir, logger_filename)


def stop_logger(output_dir=TestConf.output_dir, logger_filename=TestConf.logger_file_name):
    """
    Stops logger process
    :param output_dir: - Name of directory where output should be stored
    :param logger_filename: name of the logger file
    """
    print('#' * 20)
    print('Stopping logger...')
    print('#' * 20)
    open(root + output_dir + logger_filename, 'r').close()


def write_line(line, output_dir=TestConf.output_dir, logger_filename=TestConf.logger_file_name):
    """
    Adds line to logger file
    :param line: What to write
    :param output_dir: - Name of directory where output should be stored
    :param logger_filename: name of the logger file
    """
    with open(root + output_dir+logger_filename, 'a') as f:
        f.write(time.now()+line)

