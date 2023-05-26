from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# path = 'C:\Program Files (x86)\chromedriver.exe'
# driver = webdriver.Chrome(path)


def scrap_tweets(driver, search_key):
    try:
        driver.get(f'https://twitter.com/search?q={search_key}&src=typed_query')
        driver.implicitly_wait(10)

        def get_tweet(element):
            try:
                user = element.find_element(By.XPATH, ".//span[contains(text(), '@')]").text
                text = element.find_element(By.XPATH, ".//div[@lang]").text
                time.sleep(4)
                tweet_data = [user, text]
            except:
                tweet_data = ['user', 'text']
            return tweet_data

        user_data = []
        text_data = []
        tweets = driver.find_elements(By.XPATH, '//article[@role="article"]')
        time.sleep(4)
        for tweet in tweets:
            tweet_list = get_tweet(tweet)
            user_data.append(tweet_list[0])
            text_data.append(' '.join(tweet_list[1].split())) # reduce whitespaces before append

        driver.quit()

        df_tweets = pd.DataFrame({'user': user_data, 'text': text_data})
        df_tweets.to_csv('tweets.csv', index=False)
        print('data_frame', df_tweets)

    except Exception as e:
        print(e)


