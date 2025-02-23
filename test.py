import requests
import json


keyword = input('Enter the keyword: ')
url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2025-02-23&'
       'sortBy=popularity&'
       'apiKey=98d51cf54f524de69cf666fbd73eeab6')

response = requests.get(url)
res = json.loads(response.text)

print(res)