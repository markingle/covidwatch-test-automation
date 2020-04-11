"""
This module contains test cases for the CovidWatch App
"""

import pytest
import time
from pages.home import CovidWatchHomePage


def test_covid_app(driver):

    home_page = CovidWatchHomePage(driver)
    home_page.accept_location_permissions()
    home_page.start_logging()
    # TODO: make sure logging has started properly
    home_page.clear_logging()
    # TODO: make sure ids are cleared
    home_page.stop_logging()
    # TODO: make sure we are not logging anymore

    assert 1 == 1