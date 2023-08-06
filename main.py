from dotenv import load_dotenv
import os
from insta import InstagramBot
from time import sleep

message = 'test'
victim = '_oof.boii_'

load_dotenv()
instabot = InstagramBot(os.getenv('INSTA_USERNAME'), os.getenv('INSTA_PASSWORD'), cookiesDirectory='Z:\Coding\instagramBot\cookies')

sleep(3)
instabot.findUser(victim)
sleep(3)
inp = input('yes or no\n')

while inp == 'y' and instabot.windowIsOpen():
    instabot.sendMessage(message)
    inp = input('yes or no \n')