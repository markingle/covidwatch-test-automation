"""
This module contains shared fixtures for CovidWatch App testing.
"""

import json
import pytest
import os
import time
from appium import webdriver
import subprocess
import signal

from appium.webdriver.appium_service import AppiumService

# Globals
CONFIG_PATH = 'config'
APPIUM_SERVER_URL = "http://localhost:{}/wd/hub"

@pytest.fixture(scope='session')
def config():
    # Read all JSON config files in directory and return it as dict of dicts
    config_d = {}
    for fn in os.listdir(CONFIG_PATH):
        # Current pattern checking is "config_" is start of file and ".json" is end of file
        if fn.endswith(".json") and fn[0:7].lower() in "config_":
            with open(os.path.join(CONFIG_PATH, fn)) as config_file:
                data = json.load(config_file)
            config_d[fn.replace(".json", "").replace("config_", "")] = data
    return config_d


@pytest.fixture
def drivers(config):

    # Initialize one appium server per device
    # appium_service = AppiumService()
    # appium_service.start(args=['--address', 'localhost', '-p', "4723"])

    _drivers = {}
    _cmd_windows = []
    for port_adder, device in enumerate(config.keys()):
        _cmd_windows.append(subprocess.Popen("cmd.exe /k appium -a 0.0.0.0 -p {}".format(4723 + port_adder),
                                             creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, close_fds=True))
        # Wait for servers to initialize
        time.sleep(5)
        # Start automation service
        _drivers[device] = webdriver.Remote(APPIUM_SERVER_URL.format(4723 + port_adder), config[device])

    # Return the driver object at the end of setup
    yield _drivers

    # For cleanup, quit the driver and kill subprocesses
    for device in _drivers.keys():
        _drivers[device].quit()
    for cmd in _cmd_windows:
        cmd.send_signal(signal.CTRL_BREAK_EVENT)
        cmd.kill()

    # appium_service.stop()
