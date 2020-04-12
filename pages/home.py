"""
This module contains CovidWatchHomePage,
the page object for the CovidWatch home page.
"""

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CovidWatchHomePage:

    def __init__(self, driver):
        self.driver = driver

        self._accept_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button"
            )))

    # Navigation functions
    def accept_location_permissions(self):

        self._accept_button.click()

        self._settings_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/navigation_user_profile"
            )))

        self._start_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/start_logging"
            )))

        self._clear_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/clear"
            )))

    def start_logging(self):

        self._start_button.click()

        # Get stop button
        self._stop_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/stop_logging"
            )))


    def clear_logging(self):

        self._clear_button.click()

    def stop_logging(self):

        self._stop_button.click()

        # Wait for start button to reappear
        self._start_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/start_logging"
            )))

    def goto_settings(self):

        self._settings_button.click()

    # Test functions for asserts
    def past_permissions_state(self):

        # Make sure permissions text isnt up anymore
        return len(self.driver.find_elements_by_id(
            "com.android.packageinstaller:id/permission_message"))

    def in_default_state(self):
        # Make sure "START" button exists
        start_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/start_logging"
            )))
        return start_button.is_displayed()

    def in_logging_state(self):
        # Make sure "STOP" button exists
        stop_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/stop_logging"
            )))
        return stop_button.is_displayed()

    def in_settings_page(self):
        # Make sure "NO" button exists
        no_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/no_button"
            )))
        return no_button.is_displayed()

    def no_ids_present(self):
        return True
