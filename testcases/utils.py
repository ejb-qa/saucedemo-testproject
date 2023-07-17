# import pytest
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from main_page import MainPage_addItems
# from cart_page


#class getlocators():
# def get_element(self, driver, locator):
#         return WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, locator)))

class CountRemoveButtonsAndCartItems():

    #Count Remove buttons in Main page to check count of added items
    def count_remove_button(self, main_page):
        remove_button = main_page.get_remove_button_count()
        remove_button_count = len(remove_button)
        print("\n>Cart has: ", remove_button_count, "remove buttons")

    #Count and display items in Cart
    def count_items_in_cart (self, cart_page):
        cart_items = cart_page.verify_cart_count()
        cart_items_count = len(cart_items)
        print("Cart has:", cart_items_count, "products")
        for list in cart_items:
            print("Product/s on cart:", list.text)


class GetPriceListFromMain():

    def get_string_price_list(self, main_page):
        #gets all ".inventory_item_price" CSS_SELECTOR from main_page.py
        price_list = main_page.get_item_price_list() 
        string_price_list = []
        for i in range(len(price_list)):
            string_price_list.append(price_list[i].text)
        return string_price_list

    def get_float_price_list(self, main_page):
        price_list = main_page.get_item_price_list()
        string_price_list = []
        float_price_list = []

        for i in range(len(price_list)):
            string_price_list.append(price_list[i].text)
            price_remove_dollar_sign = string_price_list[i].replace("$", "")
            price_to_float = float(price_remove_dollar_sign)
            float_price_list.append(price_to_float)
        return float_price_list


class GetPriceListFromCart():

    def get_string_price_list(self, cart_page):
        price_list = cart_page.get_item_price_list_cart()
        string_price_list = []
        for i in range(len(price_list)):
            string_price_list.append(price_list[i].text)
        return string_price_list

    def get_float_price_list(self, cart_page):
        price_list = cart_page.get_item_price_list_cart()
        string_price_list = []
        float_price_list = []

        for i in range(len(price_list)):
            string_price_list.append(price_list[i].text)
            price_remove_dollar_sign = string_price_list[i].replace("$", "")
            price_to_float = float(price_remove_dollar_sign)
            float_price_list.append(price_to_float)
        return float_price_list
        # total_sum = sum(price_float_list)
        # print(total_sum)








#put get_element here and other re-usable functions
#like wait functions, common element interactions
#reading date from files (e.g. excel)
#custom assertions
#or test configurations (e.g. environment, test data etc)