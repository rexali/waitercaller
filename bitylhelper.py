# import urllib2
import requests
import json

TOKEN = "ff2914e3ef43f309f683795fc6b98e1361cc0840"

ROOT_URL = "https://api-ssl.bitly.com"

SHORTEN = "/v3/shorten?access_token={}&longUrl={}"

# `https://api-ssl.bitly.com/v3/shorten?access_token=XXXX&longUrl=http%3A%2F%2Fgoogle.com`

class BitlyHelper:
    def shorten_url(self, longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            response = requests.get(url)
            jr = json.loads(response)
            return jr['data']['url']
        except Exception as e:
            print("e")