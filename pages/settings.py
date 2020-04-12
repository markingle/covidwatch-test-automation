"""
This module contains CovidWatchSettingsPage,
the page object for the CovidWatch settings page.
"""

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CovidWatchSettingsPage:

    def __init__(self, driver):

        self.driver = driver

        self.no_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/no_button"
            )))

        self.yes_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/yes_button"
            )))

        self.seen_tags_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/navigation_contact_events"
            )))

    def no_notify(self):
        self.no_button.click()

    def yes_notify(self):
        self.yes_button.click()

    def goto_seen_tags(self):
        self.seen_tags_button.click()

    def in_home_page(self):
        # Make sure "START" button exists
        start_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/start_logging"
            )))
        return start_button.is_displayed()