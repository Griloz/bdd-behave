
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@when(u'User clicks "{transfer_option}" option')
def step_impl(context, transfer_option):
    context.driver.find_element(
        By.XPATH, f"//div[text() = '{transfer_option}']").click()
