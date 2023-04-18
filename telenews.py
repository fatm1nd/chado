# Parser of public telegram channels
# Public channels are accessed in web bwrower, so we can parse them

from html.parser import HTMLParser
from lxml import objectify
import requests
import xml.etree.ElementTree as ET
import re
from bs4 import BeautifulSoup


response = requests.get("https://t.me/s/sharemed",headers={"Accept": 'application/json'})

open("sharedme.txt","w").write(response.content.decode('utf-8'))


# main = objectify.fromstring(response.content[1:])

main = BeautifulSoup(response.content.decode('utf-8'),features='lxml')

posts = (main.find_all('div',attrs={"class":"tgme_widget_message_wrap"}))

for post in posts:
    print("--------------")
    messages = post.find_all('div', attrs={'class':'tgme_widget_message_text'})
    print(messages)
    for message in messages:
        print(message.text, end="\n\n")

def is_telegram_link(link):
        # Regular expression pattern for Telegram link
        pattern = r'^https:\/\/t\.me\/s\/[a-zA-Z0-9_]{5,32}$'
        
        # Check if the link matches the pattern
        if re.match(pattern, link):
            return True
        else:
            return False

class teleChannel:

    def __init__(url) -> None:
        if not is_telegram_link(url):
            raise Exception("This is not link of telegram link")


    def is_telegram_link(link):
        # Regular expression pattern for Telegram link
        pattern = r'^https:\/\/t\.me\/s\/[a-zA-Z0-9_]{5,32}$'
        
        # Check if the link matches the pattern
        if re.match(pattern, link):
            return True
        else:
            return False