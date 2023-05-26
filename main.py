from selenium import webdriver
import os
from login import login_func
from scrap import scrap_tweets

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)

twitter_email = os.environ.get('EMAIL')
twitter_phone = os.environ.get('PHONE')
twitter_password = os.environ.get('PASSWORD')


def twitter_bot():
    login_func(driver, twitter_email, twitter_password, twitter_phone)

    scrap_tweets(driver, 'python')


if __name__ == '__main__':
    twitter_bot()

