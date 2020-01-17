from selenium import webdriver

# Default timeout
timeout = 30

# Which web driver is to be used
driver = webdriver.Chrome()

# Logger file info
output_dir = '/output'
logger_file_name = '/logger.log'

# Environment
env = "http://twitter.com"