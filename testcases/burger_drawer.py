from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators_page import Locator

class Base:
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locator()
    
    def get_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

#Test Case 01 - Test Burger Menu
class BurgerDrawer(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.burger_button = self.get_element(self.locator.burger_btn)
        #cannot put all menu here (like in LoginPage class) 
        #since burger button needs to be clicked first before all menu are displayed
    
    def get_burger_button(self):
        return self.burger_button

    def get_all_item_button(self):
        #if not self.all_item_button:
        self.all_item_button = self.get_element(self.locator.all_item_btn)
        print("\nAll Item button")
        return self.all_item_button

    def get_about_button(self):
        self.about_button = self.get_element(self.locator.about_btn)
        print("About button")
        return self.about_button

    def get_logout_button(self):
        #self.driver.refresh()
        self.logout_button = self.get_element(self.locator.logout_btn)
        print("Logout button")
        return self.logout_button

    def get_reset_state_button(self):
        self.reset_state_button = self.get_element(self.locator.reset_state_btn)
        print("Reset state button")
        return self.reset_state_button

    def get_close_burger_button(self):
        self.close_burger_button = self.get_element(self.locator.close_burger_btn)
        print("Close button")
        return self.close_burger_button
