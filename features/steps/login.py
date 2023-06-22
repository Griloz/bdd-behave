from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'User is on login page')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(15)
    context.driver.get('https://demo.ebanq.com/log-in')


@when(u'User enters valid username')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[type='email']").send_keys('Demo-User')


@when(u'User enters username "{username}"')
def step_impl(context, username):
    if username != 'blank':
        context.driver.find_element(By.CSS_SELECTOR, "[type='email']").send_keys(username)


@when(u'User enters valid password')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[type='password']").send_keys('Demo-Access1')


@when(u'User enters password "{password}"')
def step_impl(context, password):
    if password != 'blank':
        context.driver.find_element(By.CSS_SELECTOR, "[type='password']").send_keys(password)


@when(u'User clicks on login button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()


@then(u'Home page displays')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.controls__logout > span').text == 'Log Out'


@when(u'User clicks on logout button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "div.controls__logout > span").click()


@then(u'Login page displays')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.heading > h1').text == 'Login'


@then(u'Text "{text}" is displayed')
def step_impl(context, text):
    sleep(5)
    assert text.lower() in context.driver.page_source.lower()