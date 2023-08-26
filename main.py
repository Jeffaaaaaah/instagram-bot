from dotenv import load_dotenv
import os
from insta import InstagramBot
from time import sleep
from random import random
from chromeDriver import Keys
from lyricFinder import lyricFinder

victim = '_oof.boii_'

lyricBot = lyricFinder()

filePath = './txt/' + input('File name (dir = ./txt/)?')
if not os.path.exists(filePath):
    print('File not Found')
    url = input('input url (https://www.azlyrics.com/lyrics/"artist"/"song"): ')
    lyricBot.findLyrics(url)
    filePath = './txt/' + lyricBot.parseFileName(url) + '.txt'

lyrics = []
with open(filePath) as f:
    lyrics = f.read().split('\n')


load_dotenv()
instabot = InstagramBot( cookiesDirectory='Z:\Coding\instagramBot\cookies', sleepDuration=4)
instabot.login(os.getenv('INSTA_USERNAME'), os.getenv('INSTA_PASSWORD'))

sleep(10 * random())
instabot.findUser(victim)
sleep(10 * random())


for line in lyrics:
    instabot.sendMessage(line)
    sleep((random() * 3) + 2)

