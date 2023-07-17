from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators_page import Locator
from selenium.webdriver.common.by import By

class Base:
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locator()
        #self.main_page = MainPage()
    
    def get_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))
    
class CartPage(Base):

    added_in_cart = ".inventory_item_name"  
    added_in_cart_price = ".inventory_item_price"

    def verify_cart_count(self):
        self.get_cart_count = self.driver.find_elements(By.CSS_SELECTOR, self.added_in_cart)
        return self.get_cart_count
    
    def select_continue_shopping_button(self):
        self.continue_shopping_button = self.get_element(self.locator.continue_shopping_button)
        return self.continue_shopping_button
    
    def get_item_price_list_cart(self):
        self.price_list_from_cart = self.driver.find_elements(By.CSS_SELECTOR, self.added_in_cart_price)
        return self.price_list_from_cart
    
    def select_checkout_button(self):
        self.checkout_button = self.get_element(self.locator.checkout_btn)
        return self.checkout_button
    
    #def continue button to checkout
    
class CheckOutStepOne(Base):

    def get_first_name_field(self):
        self.first_name = self.get_element(self.locator.checkout1_first_name)
        return self.first_name
    
    def get_last_name_field(self):
        self.last_name = self.get_element(self.locator.checkout1_last_name)
        return self.last_name
    
    def get_postal_code_field(self):
        self.postal_code = self.get_element(self.locator.checkout1_postal_code)
        return self.postal_code
        
    












#     def select_Checkout_btn(self):
#         self.get_element(self.locator.checkout1_btnFromCart).click()
#         assert True
    
#     def checkout_stepOne(self, firstName, lastName, zip):
#         self.get_element(self.locator.checkout1_firstName).send_keys(firstName)
#         self.get_element(self.locator.checkout1_lastName).send_keys(lastName)
#         self.get_element(self.locator.checkout1_zip).send_keys(zip)
#         self.get_element(self.locator.checkout1_continue).click()
#         pageTitle = self.get_element(self.locator.checkout1_title).text
#         assert pageTitle == "Checkout: Overview" 

# class calculateTotal(Base):   
#     def calculate_totalPrice(self):
#         price1_int = self.main_page.get_price_item1

                