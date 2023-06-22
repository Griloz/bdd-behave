from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# this is our repeatable setup steps before each test case
def before_scenario(context, scenario):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(15)
    context.driver.get('https://demo.ebanq.com/log-in')

    if 'login' not in scenario.name.lower():
        context.driver.find_element(By.CSS_SELECTOR, "[type='email']").send_keys('Demo-User')
        context.driver.find_element(By.CSS_SELECTOR, "[type='password']").send_keys('Demo-Access1')
        context.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        sleep(5)
    


# this is our repeatable teardown steps after each test case
def after_scenario(context, scenario):
    context.driver.quit()