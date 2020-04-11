"""
This module contains shared fixtures for CovidWatch App testing.
"""

import json
import pytest

from appium import webdriver

CONFIG_PATH = './config.json'
APPIUM_SERVER_URL = "http://localhost:4723/wd/hub"
# DEFAULT_WAIT_TIME = 10
# SUPPORTED_BROWSERS = ['chrome', 'firefox']
#
#
@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data
#
#
# @pytest.fixture(scope='session')
# def config_browser(config):
#     # Validate and return the browser choice from the config data
#     if 'browser' not in config:
#         raise Exception('The config file does not contain "browser"')
#     elif config['browser'] not in SUPPORTED_BROWSERS:
#         raise Exception(f'"{config["browser"]}" is not a supported browser')
#     return config['browser']
#
#
# @pytest.fixture(scope='session')
# def config_wait_time(config):
#     # Validate and return the wait time from the config data
#     return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def driver(config):

    # Initialize appium driver
    phonedriver = webdriver.Remote(APPIUM_SERVER_URL, config)

    # Return the driver object at the end of setup
    yield phonedriver

    # For cleanup, quit the driver
    phonedriver.quit()