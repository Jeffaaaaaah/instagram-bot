from dotenv import load_dotenv
import os
from insta import InstagramBot
from time import sleep
from random import random
from ChromeDriver import Keys
from LyricFinder import lyricFinder

victim = '_oof.boii_'



lyrics = ['hi', 'test', 'test', 'bye']


load_dotenv()
instabot = InstagramBot( cookiesDirectory='Z:\Coding\instagramBot\cookies', sleepDuration=4)
instabot.login(os.getenv('INSTA_USERNAME'), os.getenv('INSTA_PASSWORD'))

sleep(10 * random())
instabot.findUserDirectMessage(victim)
sleep(10 * random())


for line in lyrics:
    instabot.sendMessage(line)
    sleep((random() * 3) + 2)

