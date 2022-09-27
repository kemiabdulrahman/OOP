
import urllib3
import logging
from string import Template
import requests
x = requests.get('https://www.mtn.com/about/')
print(x.text)