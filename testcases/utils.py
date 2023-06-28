import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#class getlocators():
def get_element(self, driver, locator):
        return WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, locator)))