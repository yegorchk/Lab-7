import requests
import json


API_KEY = '98d51cf54f524de69cf666fbd73eeab6'


keyword = input('Enter a keyword: ')
from_date = input('Input the date you search from (year-month-day): ')
to_date = input('Input the date you search to (year-month-day): ')
url = f'https://newsapi.org/v2/everything?q={keyword}&from={from_date}&to={to_date}&sortBy=popularity&apiKey={API_KEY}'
response = requests.get(url)
res = json.loads(response.text)
if res['status'] == 'error':
    print('You are trying to request results too far in the past. Please request the results no earlier than a month before the date you enter.')
else:
    source = res['articles'][0]['source']['name']
    print(f'Source: {source}')
    author = res['articles'][0]['author']
    print(f'Author: {author}')
    title = res['articles'][0]['title']
    print(f'Title: {title}')
    url = res['articles'][0]['url']
    print(f'URL: {url}')
    content = res['articles'][0]['content']
    print(f'Content: {content}')
    publish_date = res['articles'][0]['publishedAt'][:-10]
    print(f'Publish Date: {publish_date}')