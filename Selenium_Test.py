
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('./chromedriver')

driver.get('https://forums.edmunds.com')

print(driver.title)
