from main_page import LoginPage, MainPage, BurgerDrawer


#@pytest.mark.usefixtures("chrome_browser")
class TestLogin_TC00:
    def test_burgerMenu(self, driver):

        driver.get("https://www.saucedemo.com/?ref=hackernoon.com")
        driver.implicitly_wait(3)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

class TestBurgerDrawer_TC01:
    def test_BurgerDrawer(self, driver): 
        burger = BurgerDrawer(driver)
        # main_page = MainPage(driver)
        # burger.select_BURGER_BTN()
        # burger.select_ALL_ITEM_BTN()
        # burger.select_ABOUT_BTN()
        # burger.select_LOGOUT_BTN()
        # burger.select_RESET_STATE_BTN()
        # burger.select_CLOSE_BURGER_BTN()


class TestMainPage_TC02:
    def test_addItems(self, driver):
        main_page = MainPage(driver)
        main_page.add_item1()
        main_page.add_item2()
        main_page.verify_removed_products(driver) #uses find_elements in main_page.py  
        main_page.open_cart()
        main_page.verify_cart_count(driver) 
        main_page.select_Continue_Shopping_button()

class TestMainPage_TC03:
    def test_addMoreItems(self, driver):
        main_page = MainPage(driver)
        main_page.add_item3()
        main_page.add_item4()
        main_page.open_cart()
        main_page.verify_cart_count(driver)

class TestMainPage_TC04:
    def test_getItemPrice(self, driver):       
        main_page = MainPage(driver)
        main_page.select_Continue_Shopping_button()
        main_page.verify_removed_products(driver)
        main_page.verify_cart_count(driver) 
        main_page.get_price_item1(driver)
        main_page.get_price_item2(driver)
        main_page.get_price_item3(driver)
        main_page.get_price_item4(driver)
        

# To dos
# Add assertion
# Add more Test Cases
# Put Test Cases in separate classes (1 tc = 1 method; 1 class = 1 test suite in test_SauceDemo file)
# Fix is-a has-a relationship
# Update naming conventions
# Modify github, add descriptions, test cases, work flow etc.
        