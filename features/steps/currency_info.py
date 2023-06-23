from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@when(u'User clicks on button Select account')
def step_impl(context):
    context.driver.find_element(
        By.CSS_SELECTOR, "[formcontrolname='accountId']").click()
    sleep(3)


@when(u'User selects the desired "{account}"')
def step_impl(context, account):
    context.driver.find_element(
        By.XPATH, f"//span[text()='{account}']").click()
