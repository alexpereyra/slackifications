# coding: utf-8
import requests
url = '' # Replace with slack webhook URL
data = { "text": "slackification test" }
requests.post(url, json=data)
