from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import choice
from logs.logger import logger


@when(u'User clicks on side menu "{side_menu}"')
def step_impl(context, side_menu):
    sleep(5)
    context.driver.find_element(
        By.XPATH, f"//label[text()='{side_menu}']").click()
    context.logger.info(f'Clicked on {side_menu} side menu')


@when(u'User clicks on random news title')
def step_impl(context):
    news_titles = context.driver.find_elements(
        By.CSS_SELECTOR, 'div.news-title')
    choice(news_titles).click()
    context.logger.info(f'Clicked on random news title')
