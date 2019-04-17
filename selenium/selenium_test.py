from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import sys
import time

# RETURN 1 means TEST FAILED, 0 means TEST PASSED


def get_driver():
    driver = None
    while True:
        try:
            driver = webdriver.Remote(
                command_executor='http://selenium-chrome:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
            break
        except:
            # delay for 5 seconds while selenium-chrome server comes up
            time.sleep(5)
            continue

    return driver


def close_driver(driver):
    driver.close()


def assert_equals(value, expected, test_name):
    if value != expected:
        print('{} failed. Actual: {}. Expected: {}.'.format(
            test_name, value, expected))
        return False
    return True


def test_create_account(driver):
    driver.get('http://web:8000/signup/')
    username = driver.find_element_by_name('username')
    username.send_keys(test_username)
    pword = driver.find_element_by_name('password')
    pword.send_keys(test_pword)

    driver.find_element_by_id('submit').click()

    # should redirect to home
    if not assert_equals(driver.current_url, 'http://web:8000/home/', sys._getframe().f_code.co_name):
        return 1

    return 0


# def test_login(driver):
#     driver.get('http://web:8000/login/')
#     email = driver.find_element_by_name('email')
#     email.send_keys(test_email)
#     pword = driver.find_element_by_name('password')
#     pword.send_keys(test_pword)
#     driver.find_element_by_id('submit').click()

#     # should redirect to home
#     if not assert_equals(driver.current_url, 'http://web:8000/', sys._getframe().f_code.co_name):
#         return 1

#     # make sure cookies are set correctly
#     for cookie in driver.get_cookies():
#         cookie_name = cookie.get('name', None)
#         if cookie_name == 'user_id' and not assert_equals(cookie['value'], '\"'+test_email+'\"', sys._getframe().f_code.co_name):
#             return 1
#         if cookie_name == 'auth' and cookie['value'] is None:
#             return 1

#     return 0


# def test_create_listing(driver):
#     driver.get('http://web:8000/items/create/')

#     name = driver.find_element_by_name('name')
#     name.send_keys(test_model_name)
#     color = driver.find_element_by_name('color')
#     color.send_keys(test_color)
#     price = driver.find_element_by_name('price')
#     price.send_keys(test_price)
#     size = driver.find_element_by_name('size')
#     size.send_keys(200)
#     quantity = driver.find_element_by_name('quantity')
#     quantity.send_keys(test_quantity)

#     driver.find_element_by_id('submit').click()

#     success_message = driver.find_element_by_name('alert alert-success')
#     if not assert_equals(success_message.text, 'Listing created!', sys._getframe().f_code.co_name):
#         return 1

#     return 0


# def test_check_most_recent(driver):
#     driver.get('http://web:8000/')
#     table = driver.find_element_by_name('table')

#     row = table.find_elements_by_tag_name('tr')[1]
#     # check most recent
#     if row.text is None or not assert_equals(row.text, '{} {} {} {}'.format(test_model_name, test_color, float(test_price), test_email), sys._getframe().f_code.co_name):
#         return 1

#     return 0


# def test_check_details_page(driver):
#     driver.get('http://web:8000/details/')
#     table = driver.find_element_by_name('table')

#     # check details page is correct
#     rows = table.find_elements_by_tag_name('tr')
#     i = len(rows) - 1
#     while i >= 1:
#         if rows[i].text is None or not assert_equals(rows[i].text, '{} {} {} {} {}'.format(test_model_name, test_color, float(test_price), test_quantity, test_email), sys._getframe().f_code.co_name):
#             return 1
#         i -= 1
#         break

#     return 0


# def test_search(driver):
#     driver.get('http://web:8000/')
#     search = driver.find_element_by_name('q')
#     search.send_keys(test_model_name)

#     driver.find_element_by_id('button').click()

#     time.sleep(5)

#     table = driver.find_element_by_name('table')

#     row = table.find_elements_by_tag_name('tr')[1]
#     # check result
#     if row.text is None or not assert_equals(row.text, '{} {} {} {} {}'.format(test_model_name, test_color, float(test_price), test_quantity, test_email), sys._getframe().f_code.co_name):
#         return 1

#     return 0


# def test_logout(driver):
#     driver.get('http://web:8000/logout/')
#     # returns you to login page
#     if not assert_equals(driver.current_url, 'http://web:8000/login/', sys._getframe().f_code.co_name):
#         return 1

#     success_message = driver.find_element_by_name('alert alert-success')
#     if not assert_equals(success_message.text, 'Logged out successfully!', sys._getframe().f_code.co_name):
#         return 1

#     for cookie in driver.get_cookies():
#         cookie_name = cookie.get('name', None)
#         # make sure there's no auth left
#         if cookie_name == 'auth' and cookie['value'] is not None:
#             print('{} failed! There\'s still an auth!!'.format(
#                 sys._getframe().f_code.co_name))
#             return 1

#     return 0


# Constants ------------------------------------------------------------------------------ #
test_username = 'test_username'
test_pword = 'password'
# test_model_name = 'an item'
# test_color = 'a color'
# test_price = 100
# test_quantity = 1000
#  --------------------------------------------------------------------------------------- #

failed_tests = 0
driver = get_driver()
# --- add tests here ----
failed_tests += test_create_account(driver)
# failed_tests += test_login(driver)
# failed_tests += test_create_listing(driver)
# failed_tests += test_check_most_recent(driver)
# failed_tests += test_check_details_page(driver)
# failed_tests += test_search(driver)
# failed_tests += test_logout(driver)
# -----------------------
close_driver(driver)

if failed_tests == 0:
    print('ALL TESTS PASSED.')
else:
    print('{} TESTS FAILED!!'.format(failed_tests))
    sys.exit(1)
