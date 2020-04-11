"""
This module contains test cases for the CovidWatch App
"""

import pytest
import time
from pages.home import CovidWatchHomePage
from pages.settings import CovidWatchSettingsPage


def test_covid_app(driver):

    # Home page testing
    home_page = CovidWatchHomePage(driver)
    home_page.accept_location_permissions()
    home_page.start_logging()
    # TODO: make sure logging has started properly
    home_page.clear_logging()
    # TODO: make sure ids are cleared
    home_page.stop_logging()
    # TODO: make sure we are not logging anymore
    home_page.goto_settings()
    # TODO: make sure transitioned to settings

    # Settings page testing
    settings_page = CovidWatchSettingsPage(driver)
    settings_page.yes_notify()
    # TODO: make sure we are notifying
    settings_page.no_notify()
    # TODO: make sure wwe are not notifying
    settings_page.goto_seen_tags()
    # TODO: Make sure back on seen tags

    assert 1 == 1