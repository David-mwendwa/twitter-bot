from selenium.webdriver.common.by import By
import time

# path = 'C:\Program Files (x86)\chromedriver.exe'
# driver = webdriver.Chrome(path)


def login_func(driver, twitter_email, twitter_password, twitter_phone):
    try:
        driver.get('https://twitter.com/login')
        driver.implicitly_wait(5)

        driver.maximize_window()

        # enter username
        username = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
        username.send_keys(twitter_email)
        time.sleep(4)

        # click next button
        next_btn = driver.find_element(By.XPATH, '//span[contains(text(), "Next")]')
        next_btn.click()
        time.sleep(4)
        driver.implicitly_wait(5)

        unusual_activity_detected = driver.find_element(By.XPATH, '//span[contains(text(), "unusual login")]')
        if unusual_activity_detected:
            # enter phone
            phone = driver.find_element(By.XPATH, '//input[@autocomplete]')
            phone.send_keys(twitter_phone)
            time.sleep(4)

            # click next button
            next_btn = driver.find_element(By.XPATH, '//span[contains(text(), "Next")]')
            next_btn.click()
            time.sleep(4)
            driver.implicitly_wait(5)

        # enter password
        password = driver.find_element(By.XPATH, '//input[@name="password"]')
        password.send_keys(twitter_password)
        time.sleep(4)

        # click login button
        login_btn = driver.find_element(By.XPATH, '(//div[@role="button"])[3]')
        login_btn.click()
        time.sleep(4)

    except Exception as e:
        print(e)


