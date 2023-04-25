# Parser of public telegram channels
# Public channels are accessed in web bwrower, so we can parse them

from html.parser import HTMLParser
from lxml import objectify
import requests
import xml.etree.ElementTree as ET
import re
from bs4 import BeautifulSoup
import re


response = requests.get("https://t.me/s/sharemed",
                        headers={"Accept": 'application/json'})

open("sharedme.txt", "w").write(response.content.decode('utf-8'))


# main = objectify.fromstring(response.content[1:])

# main = BeautifulSoup(response.content.decode('utf-8'), features='lxml')

# posts = (main.find_all('div', attrs={"class": "tgme_widget_message"}))

# alias = "https://t.me/s/sharemed"[15:]
# print(alias)



# for post in posts:
#     print(f"-------{post['data-post']}-------")

#     reg = "(?:\(['\"]?)(.*?)(?:['\"]?\))"

#     textMessages = post.find_all(
#         'div', attrs={'class': 'tgme_widget_message_text'})
#     pictures = post.find_all('a', attrs={'class': 'tgme_widget_message_photo_wrap'})
#     # print(*pictures, sep="\n")
#     for picture in pictures:
#         urlP = re.search(reg,picture['style']).group(1)
#         print(urlP)

#     print("   --Videos--")
#     for video in post.find_all('video'):
#         print(video['src'])
#     print()
#     for message in list(set(textMessages)):
#         print(message.text, end="\n\n")

        


class teleChannel:

    '''

    '''

    url = ""
    channelPic = ""
    title = ""

    posts = {}

    def __init__(self, url) -> None:
        if not self.is_telegram_link(url):
            raise Exception("This is not link of telegram link")
        self.url = url

        response = requests.get("https://t.me/s/sharemed",
                        headers={"Accept": 'application/json'})

        main = BeautifulSoup(response.content.decode('utf-8'), features='lxml')

        self.channelPic = (main.find('img'))

        self.title = (main.find('div', attrs={"class":"tgme_channel_info_header_title"}).text)

        postsRaw = (main.find_all('div', attrs={"class": "tgme_widget_message"}))
        
        alias = url[15:]


        # print(alias)
        for post in postsRaw:
            # print(f"-------{post['data-post']}-------")
            postId = post['data-post'][len(alias) + 1:]
            reg = "(?:\(['\"]?)(.*?)(?:['\"]?\))"
            self.posts[postId] = {}
            textMessages = post.find_all(
                'div', attrs={'class': 'tgme_widget_message_text'})
            pictures = post.find_all('a', attrs={'class': 'tgme_widget_message_photo_wrap'})
            # print(*pictures, sep="\n")
            self.posts[postId]['pictures'] = []
            for picture in pictures:
                self.posts[postId]['pictures'].append(re.search(reg,picture['style']).group(1))
            self.posts[postId]['videos'] = []
            for video in post.find_all('video'):
                self.posts[postId]['videos'].append(video['src'])
            for message in list(set(textMessages)):
                self.posts[postId]['text'] = message.text
                # print(message.text, end="\n\n")


    def is_telegram_link(self,link):
        # Regular expression pattern for Telegram link
        pattern = r'^https:\/\/t\.me\/s\/[a-zA-Z0-9_]{5,32}$'

        # Check if the link matches the pattern
        if re.match(pattern, link):
            return True
        else:
            return False
    
    # def getLastPost(self):
    #     return self.posts[0]



tch = teleChannel("https://t.me/s/sharemed")
print(tch.posts)
