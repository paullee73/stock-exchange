from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import sys
import time
from selenium.webdriver.common.by import By


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


def access_signup(driver):
    driver.get('http://web:8000/signup')
    if not assert_equals(driver.current_url, 'http://web:8000/signup', sys._getframe().f_code.co_name):
        return 1

    return 0


# Constants
test_username = 'test_username'
test_pword = 'password'

failed_tests = 0
driver = get_driver()


# tests
failed_tests += access_signup(driver)
close_driver(driver)

if failed_tests == 0:
    print('ALL TESTS PASSED.')
else:
    print('{} TESTS FAILED'.format(failed_tests))
    sys.exit(1)
