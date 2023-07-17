# import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators_page import Locator

#Page object element (Page class/Page object)

class Base:
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locator()
    
    def get_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))


class LoginPage(Base):
    
    def __init__(self, driver):
        #self.driver = driver
        super().__init__(driver)
        self.username = self.get_element(self.locator.username_field)
        self.password = self.get_element(self.locator.password_field)
        self.login_button = self.get_element(self.locator.login_btn)

    def get_username_field(self):
        return self.username

    def get_password_field(self):
        return self.password

    def get_login_button(self):
        return self.login_button


class MainPageAddItems(Base):
  
    #Locators for find_elements //because find_elements does not support self.locator.<locator>?
    removed_buttons = ".btn.btn_secondary.btn_small.btn_inventory" 

    def get_item1_add_button(self):
        self.add_item1 = self.get_element(self.locator.add_to_cart_item1)
        return self.add_item1
    
    def get_item2_add_button(self):
        self.add_item2 = self.get_element(self.locator.add_to_cart_item2)
        return self.add_item2
    
    def get_item3_add_button(self):
        self.add_item3 = self.get_element(self.locator.add_to_cart_item3)
        return self.add_item3
    
    def get_item4_add_button(self):
        self.add_item4 = self.get_element(self.locator.add_to_cart_item4)
        return self.add_item4
    
    def get_remove_button_count(self):
        self.count_remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, self.removed_buttons)
        return self.count_remove_buttons
    
    def select_cart_button(self):
        self.cart_button = self.get_element(self.locator.cart_button)
        return self.cart_button
    

class MainPageItemPrice(Base):
    itemPrices = ".inventory_item_price"

    def __init__(self, driver):
        super().__init__(driver)
        self.item1 = self.get_element(self.locator.item1_price_text)

    def get_item_price_list(self):
        
        self.itemPriceList = self.driver.find_elements(By.CSS_SELECTOR, self.itemPrices)
        return self.itemPriceList
        


 















# #Test Case 02.a - Add 2 products in Products page and verify changes by counting Remove button and Items displayed in Cart page
#     def add_item1(self):
#         self.get_element(self.locator.add_to_cart_item1).click()
#         assert True
  
#     def add_item2(self):
#         self.get_element(self.locator.add_to_cart_item2).click()
#         assert True

#     def verify_removed_products(self, driver):
#          removed_count = self.driver.find_elements(By.CSS_SELECTOR, self.removed_buttons)
#          time.sleep(2)
#          print("\n>Cart has: ", len(removed_count), "remove buttons")

#     def open_cart(self):
#         self.get_element(self.locator.cart_button).click()
#         assert True
    
#     #do not include for now
#     def verify_cart_count(self, driver):
#         cart_count = self.driver.find_elements(By.CSS_SELECTOR, self.added_in_cart)
#         time.sleep(2)
#         print(">Cart has: ", len(cart_count), "products")
#         for list in cart_count:
#             print("Product/s on cart:", list.text)

#     #do not include for now
#     def select_Continue_Shopping_button(self):
#         self.get_element(self.locator.continue_shopping_button).click()
#         assert True


# #Test Case 03 - Add 2 more items and verify changes in Cart page
#     def add_item3(self):
#         self.get_element(self.locator.add_to_cart_item3).click()
#         assert True
    
#     def add_item4(self):
#         self.get_element(self.locator.add_to_cart_item4).click()
#         assert True
# #then reuse open_cart, verify_cart_count for TC 03


# #Test Case 04 - Go back to Products page and verify Price of items added
# #reuse select_Continue_Shopping_button, verify_removed_products 

#     def get_price_item1 (self, driver):
#         item1_text = self.get_element(self.locator.item1_price_text).text
#         item1_text = item1_text.replace("$", "")  # Remove the "$" character
#         item1_price_int = float(item1_text) #use int if integer only
#         assert item1_price_int == 29.99, "Error: Incorrect price for Item 1"
        
#     def get_price_item2 (self, driver):
#         item2_text = self.get_element(self.locator.item2_price_text).text
#         item2_text = item2_text.replace("$", "")  
#         item2_price_int = float(item2_text) 
#         assert item2_price_int == 9.99, "Error: Incorrect price for Item 2"
    
#     def get_price_item3 (self, driver):
#         item3_text = self.get_element(self.locator.item3_price_text).text
#         item3_text = item3_text.replace("$", "")  
#         item3_price_int = float(item3_text) 
#         assert item3_price_int == 15.99, "Error: Incorrect price for Item 3"
    
#     def get_price_item4 (self, driver):
#         item4_text = self.get_element(self.locator.item4_price_text).text
#         item4_text = item4_text.replace("$", "")  
#         item4_price_int = float(item4_text) 
#         assert item4_price_int == 49.99, "Error: Incorrect price for Item 4"

# self.driver = driver
# main_page = MainPage(driver)
# product1_price = main_page.get_price_item1(driver)
# print(product1_price)



        





    
        
    



    