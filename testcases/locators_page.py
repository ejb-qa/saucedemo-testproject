from selenium.webdriver.common.by import By

class Locator:
    #Locators for Login Page
    username_field = (By.XPATH, "//input[@id='user-name']")
    password_field = (By.XPATH, "//input[@id='password']")
    login_btn = (By.XPATH, "//input[@id='login-button']")  

    #Locators for Burger Menu
    burger_btn = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    all_item_btn = (By.XPATH, "//a[@id='inventory_sidebar_link']")
    about_btn = (By.XPATH, "//a[@id='about_sidebar_link']")
    logout_btn = (By.XPATH, "//a[@id='logout_sidebar_link']")
    reset_state_btn = (By.XPATH, "//a[@id='reset_sidebar_link']")
    close_burger_btn = (By.XPATH, "//button[@id='react-burger-cross-btn']")

    #Locators for Products Page and Cart
    add_to_cart_item1 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    add_to_cart_item2 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
        #removed_buttons = (By.CSS_SELECTOR, ".btn.btn_secondary.btn_small.btn_inventory")  --find_elements doesn't support self.locator...
    cart_button = (By.XPATH,"//a[@class='shopping_cart_link']")
        #added_in_cart = (By.CSS_SELECTOR, ".inventory_item_name") --find_elements doesn't support self.locator...
    continue_shopping_button = (By.XPATH, "//button[@id='continue-shopping']")
    add_to_cart_item3 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    add_to_cart_item4 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    removed_buttons = (By.XPATH, ".btn.btn_secondary.btn_small.btn_inventory")
    item1_price_text = (By.XPATH, "//div[@class='inventory_list']//div[1]//div[2]//div[2]//div[1]")     #"inventory_item_price"
    item2_price_text = (By.XPATH, "//div[@id='inventory_container']//div[2]//div[2]//div[2]//div[1]")   #used Rel XPATH)
    item3_price_text = (By.XPATH, "(//div[@class='inventory_item_price'][normalize-space()='$15.99'])[1]")  #used index XPATH)
    item4_price_text = (By.XPATH, "(//div[@class='inventory_item_price'][normalize-space()='$49.99'])[1]")

    checkout_btn = (By.XPATH, "//button[@id='checkout']")

    checkout1_first_name = (By.XPATH, "//input[@id='first-name']")
    checkout1_last_name = (By.XPATH, "//input[@id='last-name']")
    checkout1_postal_code = (By.XPATH, "//input[@id='postal-code']")
    checkout1_continue = (By.XPATH, "//input[@id='continue']")
    checkout1_cancel = (By. XPATH, "//button[@id='cancel']")
    checkout1_title = (By.XPATH, "//span[@class='title']")
