from main import *

from dotenv import load_dotenv
import os

class bot:
    def __init__(self, username, password, sleepDuration=2) -> None:
        self.username = username
        self.password = password
        self.sleepDuration = sleepDuration
        self.victim = victim
        self.message = message
        self.baseUrl = 'https://instagram.com'
        self.dmUrl = 'https://www.instagram.com/direct/inbox/'
        self.bot = driver
        

    def login(self):
    
        self.bot.get(self.baseUrl)
        
        # ENTERING THE USERNAME FOR LOGIN INTO INSTAGRAM
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
    
        enter_username.send_keys(self.username)
        
        # ENTERING THE PASSWORD FOR LOGIN INTO INSTAGRAM
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
    
        # RETURNING THE PASSWORD and login into the account
        enter_password.send_keys(Keys.RETURN)
        
        #sleep to make look less bot like
        sleep(self.sleepDuration)
        popup1 = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located(("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))).click()

        sleep(self.sleepDuration)
        popup2 = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located(("xpath", '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))).click()
        
       


    def findUser(self, user=''):
        #redirects to dms
        self.bot.get(self.dmUrl)

        #clicks on new message button
        newMessage = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located(('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div'))).click()
        
        sleep(self.sleepDuration)
        
        #inputs username into search bar
        search = self.bot.switch_to.active_element
        search.send_keys(user)

        sleep(self.sleepDuration)
    
        # click on the username
        #self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]').click()
        usernameResult = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located(('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]'))).click()
        sleep(self.sleepDuration)
    
        # next button
        chatButton = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located(('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div'))).click()
        
        
    
    def sendMessage(self, messsage=''):
        # click on message area
        send = self.bot.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
    
        # types message
        send.send_keys(message)
        sleep(self.sleepDuration)
    
        # send message
        send.send_keys(Keys.RETURN)
        sleep(self.sleepDuration)
    
    

message = 'test'
victim = '_oof.boii_'

load_dotenv()
instabot = bot(os.getenv('INSTA_USERNAME'), os.getenv('INSTA_PASSWORD'))
instabot.login()
sleep(3)
instabot.findUser(victim)
sleep(3)
input = input('yes or no\n')

while input == 'y':
    instabot.sendMessage(message)
    input = input('yes or no \n')
