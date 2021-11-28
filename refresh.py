import requests
import time

URL = "https://zerodha-test1.herokuapp.com/welcome"

while True:
    r = requests.get(url = URL)
    time.sleep(25)
