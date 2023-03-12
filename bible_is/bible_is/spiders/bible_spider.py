import requests
import time
from bs4 import BeautifulSoup

url = 'http://live.bible.is/bible/BDQDVS/MAT/1'

while True:
    # Set user agent and proxy
    headers = {
        'User-Agent': 'Bot-1.0'
    }
    proxies = {
        'http': 'http://123.45.67.89:8080',
        'https': 'https://123.45.67.89:8080'
    }

    # Send request and parse response
    response = requests.get(url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.content, 'html.parser')
    verses = soup.select('.chapter-justify')
    for verse in verses:
        verse_number = verse.select_one('.verseNumber').text.strip()
        verse_text = verse.select_one('.verseText').text.strip()
        print(f"{verse_number}: {verse_text}")

    # Change user agent and proxy every 30 seconds
    time.sleep(30)
    headers = {
        'User-Agent': 'Bot-2.0'
    }
    proxies = {
        'http': 'http://12.34.56.78:8080',
        'https': 'https://12.34.56.78:8080'
    }
