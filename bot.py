"""
Cryptocurrency Twitter Bot.

Get data from CoinMarketCap and publish on Twitter.

Author: Bruno Santos
"""

import os
import time
import twitter
import requests


api = twitter.Api( consumer_key        = os.environ['consumer_key'],
                   consumer_secret     = os.environ['consumer_secret'],
                   access_token_key    = os.environ['access_token_key'],
                   access_token_secret = os.environ['access_token_secret'])

BTC_api_url = 'https://api.coinmarketcap.com/v2/ticker/1/'
ETH_api_url = 'https://api.coinmarketcap.com/v2/ticker/1027/'

sleep = 300

while True:
    USD = requests.get(BTC_api_url).json()['data']['quotes']['USD']['price']
    print('1 BTC = %s USD' % USD)
    api.PostUpdate('1 BTC = %s USD #bitcoin #cryptocurrency #blockchain' % USD)
    time.sleep(sleep)

    USD = requests.get(ETH_api_url).json()['data']['quotes']['USD']['price']
    print('1 ETH = %s USD' % USD)
    api.PostUpdate('1 ETH = %s USD #ethereum #cryptocurrency #blockchain' % USD)
    time.sleep(sleep)
