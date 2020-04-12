"""
This module contains test cases for the CovidWatch App
"""

import pytest
import time
from pages.home import CovidWatchHomePage
from pages.settings import CovidWatchSettingsPage


def test_single_device(drivers):

    # TODO: convert to parallel test with pass/fail for each device
    for driver in drivers.values():

        # Home page testing
        home_page = CovidWatchHomePage(driver)
        home_page.accept_location_permissions()
        assert home_page.past_permissions_state() == 0
        home_page.start_logging()
        assert home_page.in_logging_state() is True
        home_page.clear_logging()
        assert home_page.no_ids_present() is True
        home_page.stop_logging()
        assert home_page.in_default_state() is True
        home_page.goto_settings()
        assert home_page.in_settings_page() is True

        # Settings page testing
        settings_page = CovidWatchSettingsPage(driver)
        settings_page.yes_notify()
        # TODO: make sure we are notifying
        settings_page.no_notify()
        # TODO: make sure we are not notifying
        settings_page.goto_seen_tags()
        assert settings_page.in_home_page() is True

def test_n_devices(drivers):

    pass