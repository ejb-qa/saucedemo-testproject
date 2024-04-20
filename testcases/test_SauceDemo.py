from main_page import LoginPage, MainPageAddItems, MainPageItemPrice
from burger_drawer import BurgerDrawer
from cart_page import CartPage, CheckOutStepOne
import time
from utils import CountRemoveButtonsAndCartItems, GetPriceListFromCart, GetPriceListFromMain
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Test Cases

class TestLogin:
    def test_login(self, driver):
        # self.driver = driver

        driver.get("https://www.saucedemo.com/?ref=hackernoon.com")
        driver.implicitly_wait(3)

        login_page = LoginPage(driver)

        username = login_page.get_username_field()
        username.send_keys("standard_user")

        password = login_page.get_password_field()
        password.send_keys("secret_sauce")

        login_button = login_page.get_login_button()
        login_button.click()

        assert "Swag" in driver.title
        # pageTitle = self.driver.title
        # #assert "pageTitle" == "Swag Labs"


# Test Case for checking if buttons in Burger Drawer are displayed
class TestBurgerDrawer:
    def test_burger_drawer(self, driver): 
        # self.driver = driver 
        driver.implicitly_wait(5)

        burger = BurgerDrawer(driver)
        # burger.get_burger_menu(driver)

        burger_button = burger.get_burger_button()
        assert burger_button.is_displayed(), "Error: Burger button/menu is not displayed"
        burger_button.click()

        all_item_button = burger.get_all_item_button()
        assert all_item_button.is_displayed(), "Error: All Item button is not displayed"
       
        about_button = burger.get_about_button()
        about_button.click()
        driver.implicitly_wait(3)
        print("You're currently in page:" , driver.current_url)
        assert "saucelabs" in driver.current_url, "Error: About button not displayed/selected" 
        driver.back()
        print("Back to Main page")

        #added this part to fix the StaleElement error since the page was "refreshed" 
        #and cannot find the elements after going to About page
        burger = BurgerDrawer(driver)
        burger_button = burger.get_burger_button()
        assert burger_button.is_displayed(), "Error: Burger button/menu is not displayed"
        burger_button.click()

        logout_button = burger.get_logout_button()
        print(logout_button)
        assert logout_button.is_displayed(), "Error: Logout button is not displayed" 

        reset_state_button = burger.get_reset_state_button()
        assert reset_state_button.is_displayed(), "Error: Reset State button is not displayed"

        close_burger_button = burger.get_close_burger_button()
        close_burger_button.click()
        time.sleep(2) 


#Test Case for adding items to Cart
class TestMainPage:

    def test_add_Items(self, driver):
        driver.implicitly_wait(3)

        main_page = MainPageAddItems(driver)
        cart_page = CartPage(driver)
        count_removeBtn_and_cartItems = CountRemoveButtonsAndCartItems()

        item_button_1 = main_page.get_item1_add_button()
        assert item_button_1.is_displayed(), "Error: Item1 not displayed"
        item_button_1.click()

        item_button_2 = main_page.get_item2_add_button()
        assert item_button_2.is_displayed(), "Error: Item2 not displayed"
        item_button_2.click()
        
        count_removeBtn_and_cartItems.count_remove_button(main_page)

        cart_button = main_page.select_cart_button()
        assert cart_button.is_displayed(), "Error: Cart is not displayed"
        cart_button.click()
        
        count_removeBtn_and_cartItems.count_items_in_cart(cart_page)
 
        continue_shopping_button = cart_page.select_continue_shopping_button()
        continue_shopping_button.click()

#add more items
    def test_add_more_items(self, driver):

        main_page = MainPageAddItems(driver)
        cart_page = CartPage(driver)
        count_removeBtn_and_cartItems = CountRemoveButtonsAndCartItems()

        item_button_3 = main_page.get_item3_add_button()
        assert item_button_3.is_displayed(), "Error: Item3 not displayed"
        item_button_3.click()

        item_button_4 = main_page.get_item4_add_button()
        assert item_button_4.is_displayed(), "Error: Item4 not displayed"
        item_button_4.click()

        count_removeBtn_and_cartItems.count_remove_button(main_page)

        cartButton = main_page.select_cart_button()
        assert cartButton.is_displayed(), "Error: Cart is not displayed"
        cartButton.click()
        
        count_removeBtn_and_cartItems.count_items_in_cart(cart_page)

        continue_shopping_button = cart_page.select_continue_shopping_button()
        continue_shopping_button.click()


#Test Case for getting price of items  (first 4) in Main Page    
class TestGetPriceFromMainPage:
    
    def test_get_float_price_list_from_main  (self, driver):
        main_page = MainPageItemPrice(driver)
        price_list = GetPriceListFromMain()
        
        float_price_list = price_list.get_float_price_list(main_page)
        print(float_price_list[0:4])
        total_sum = sum(float_price_list[0:4])
        print("Total sum:", total_sum)


class TestGetPriceFromCartPage:

    def test_get_float_price_list_from_cart(self, driver):
        main_page = MainPageAddItems(driver)
        cart_page = CartPage(driver)
        price_list = GetPriceListFromCart()
        
        cart_button = main_page.select_cart_button()
        cart_button.click()

        float_price_list = price_list.get_float_price_list(cart_page)
        print(float_price_list)
        total_sum = sum(float_price_list)
        print("Total sum:", total_sum)
        time.sleep(2)


class TestCheckOut:

    def test_checkout_step_one(self, driver):
        cart_page = CartPage(driver)
        check_out_information = CheckOutStepOne(driver)

        checkout_button = cart_page.select_checkout_button()
        checkout_button.click()

        first_name = check_out_information.get_first_name_field()
        first_name.send_keys("Harry")

        last_name = check_out_information.get_last_name_field()
        last_name.send_keys("Potter")

        postal_code = check_out_information.get_postal_code_field()
        postal_code.send_keys("934")

        print("Chekout details entered")




        
 

 





























#==================================================

    #     main_page.add_item2()
    #    # /main_page.verify_removed_products(driver) #uses find_elements in main_page.py  
    #     main_page.open_cart()
#        # / main_page.verify_cart_count(driver) 
#        # / main_page.select_Continue_Shopping_button()
#         cart_page.select_Checkout_btn()
#         time.sleep(2)
#         cart_page.checkout_stepOne("Harry", "Potter", "934")


        




# To dos
# Add assertion/
# Add more Test Cases (with assertion) / calculate total, update items, deleted items (E2E)
# Put Test Cases in separate classes (1 tc = 1 method; 1 class = 1 test suite in test_SauceDemo file)
# Fix is-a has-a relationship
# Update naming conventions
# Modify github, add descriptions, test cases, work flow etc.
# Add exceptions
# Use list
        
