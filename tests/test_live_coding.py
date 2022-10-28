from selenium import webdriver
from testdata import test_data
from pages.home import Home
from pages.contact_us import ContactUs
from lib.helpers import Helper
from pages.sign_in import SignIn
from pages.sign_up import SignUp

new_email, new_pass = "", ""
driver = webdriver.Chrome()
helper = Helper(driver)
sign_in = SignIn(driver)
sign_up = SignUp(driver)
home = Home(driver)
contact_us = ContactUs(driver)


def test_1_registration():
    global new_email
    global new_pass
    new_email, new_pass = sign_up.create_new_account()


def test_2_sign_in():
    sign_in.login(new_email, new_pass)


def test_3_contact_us_success():
    contact_us.send_message_to_support(message="Some message to support")


def test_4_contact_us_error():
    contact_us.send_message_to_support()


def test_5_woman_dresses():
    home.click_dresses_tab()
    home.get_product_names_and_prices()


if __name__ == '__main__':
    # Pre-condition:
    helper.go_to_page(test_data.main_url)

    test_1_registration()
    home.click_sign_out()
    test_2_sign_in()
    test_3_contact_us_success()
    test_4_contact_us_error()
    test_5_woman_dresses()

    # post-condition
    helper.driver.quit()
