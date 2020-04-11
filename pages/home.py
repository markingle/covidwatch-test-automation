"""
This module contains CovidWatchHomePage,
the page object for the CovidWatch home page.
"""

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CovidWatchHomePage:

    def __init__(self, driver):
        self.driver = driver

        self.accept_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button"
            )))

    def accept_location_permissions(self):

        self.accept_button.click()

        self.settings_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/navigation_user_profile"
            )))

        self.start_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/start_logging"
            )))

        self.clear_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/clear"
            )))

    def start_logging(self):

        self.start_button.click()

        # Get stop button
        self.stop_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/stop_logging"
            )))


    def clear_logging(self):

        self.clear_button.click()

    def stop_logging(self):

        self.stop_button.click()

        # Wait for start button to reappear
        self.start_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "org.covidwatch.tags.android:id/start_logging"
            )))

    def goto_settings(self):

        self.settings_button.click()