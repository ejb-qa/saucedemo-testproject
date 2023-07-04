import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    r_options = Options()
    r_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=r_options)
    
    # testUrl: str = "https://www.saucedemo.com/?ref=hackernoon.com"
    # driver.get(testUrl)
    # driver.implicitly_wait(3)
    # print(driver.title)

    #print("\nLaunch browser")

    yield driver
    driver.close()

