from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@when(u'User clicks on my profile Section')
def step_impl(context):
    sleep(5)
    context.driver.find_element(
        By.XPATH, "//label[text()='My Profile']").click()  # //div[6]/label  //label[text()='My Profile']


# @then(u'Summary section should display')
# def step_impl(context):
#     sleep(5)
#     assert 'Summary' in context.driver.page_source
    # context.driver.quit()
