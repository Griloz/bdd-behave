from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from configs import config
from datetime import datetime
from logs.logger import logger

# this is our repeatable setup steps before each test case


def before_all(context):
    context.logger = logger
    context.logger.info(
        '################## START TEST EXECUTION ##################')


def after_all(context):
    context.logger.info(
        '################## END TEST EXECUTION ##################')


def before_scenario(context, scenario):
    context.logger.info(f'------ Test Case: {scenario.name} ------')
    context.driver = webdriver.Firefox()
    context.logger.info(f'Opened the {context.driver.name}')
    context.driver.implicitly_wait(config.TIMEOUT)
    context.driver.get(config.URL)
    context.logger.info(f'Navigated to {config.URL}')

    if 'login' not in scenario.name.lower():
        context.driver.find_element(
            By.CSS_SELECTOR, "[type='email']").send_keys(config.username)
        context.driver.find_element(
            By.CSS_SELECTOR, "[type='password']").send_keys(config.password)
        context.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        context.logger.info(
            f'Trying to login with username = {config.username} and password = {config.password}')
        sleep(5)


# this is our repeatable teardown steps after each test case
def after_scenario(context, scenario):
    timestamp = datetime.now().strftime('%m%d%y_%H%M%S')
    context.driver.save_screenshot(
        fr".\evidence\{scenario.name}_{timestamp}.png")
    context.driver.quit()
    context.logger.info('Closed the browser')
