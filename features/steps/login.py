from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from configs import config


@given(u'User is on login page')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(config.TIMEOUT)
    context.driver.get(config.URL)


@when(u'User enters valid username')
def step_impl(context):
    context.driver.find_element(
        By.CSS_SELECTOR, "[type='email']").send_keys(config.username)


@when(u'User enters username "{username}"')
def step_impl(context, username):
    # if username == 'blank':
    #     username = ''
    if username != 'blank':
        context.driver.find_element(
            By.CSS_SELECTOR, "[type='email']").send_keys(username)


@when(u'User enters valid password')
def step_impl(context):
    context.driver.find_element(
        By.CSS_SELECTOR, "[type='password']").send_keys(config.password)


@when(u'User enters password "{password}"')
def step_impl(context, password):
    if password != 'blank':
        context.driver.find_element(
            By.CSS_SELECTOR, "[type='password']").send_keys(password)


@when(u'User clicks on login button')
def step_impl(context):
    context.driver.find_element(
        By.CSS_SELECTOR, "[type='submit']").click()


@then(u'Home page displays')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, 'div.controls__logout > span').text == 'Log Out'
    # context.driver.quit()


@when(u'User clicks on logout button')
def step_impl(context):
    context.driver.find_element(
        By.CSS_SELECTOR, "div.controls__logout > span").click()


@then(u'Login page displays')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, 'div.heading > h1').text == 'Login'


@then(u'Text "{text}" is displayed')
def step_impl(context, text):
    sleep(5)
    context.logger.info(
        f'Cheking if [{text}] is on the page {context.driver.current_url}')
    assert text.lower() in context.driver.page_source.lower()
    # context.driver.quit()
