import os
from login import login_func

twitter_email = os.environ.get('EMAIL')
twitter_phone = os.environ.get('PHONE')
twitter_password = os.environ.get('PASSWORD')


def twitter_bot():
    login_func(twitter_email, twitter_password, twitter_phone)


if __name__ == '__main__':
    twitter_bot()

