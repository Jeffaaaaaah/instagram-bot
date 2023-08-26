from chromeDriver import *
from time import sleep
from enum import Enum

class State(Enum):
    INITIALIZED = 0
    LOGGED_IN = 1
    LOGGED_OUT = 2
    USER_FOUND = 3

URLS = {'HomePage' : 'https://instagram.com',
        'DirectMessageInbox' : 'https://www.instagram.com/direct/inbox/'
        }


class InstagramBot:
    def __init__(self, cookiesDirectory=None, sleepDuration=2, timeOutDuration=20) -> None:
        self.URLS = URLS
        self.CACHE = {}
        self.STATE = None
        
        self.sleepDuration = sleepDuration
        
        
        if cookiesDirectory != None:
            self.isUsingCookies = True
        else:
            self.isUsingCookies = False
        self.driver = initChromeDriver(fullScreen=True, headLess=False, cookiesDirectory=cookiesDirectory)
        self.wait = WebDriverWait(self.driver, timeOutDuration)

        
        

    def login(self, username, password):
        self.driver.get(self.URLS['HomePage'])

        if self.isUsingCookies:
            timeOut = 5
        else:
            timeOut = 20

        try:
            # ENTERING THE USERNAME FOR LOGIN INTO INSTAGRAM
            enter_username = WebDriverWait(self.driver, timeOut).until(
                expected_conditions.presence_of_element_located((By.NAME, 'username')))
        
            enter_username.send_keys(username)
            
            # ENTERING THE PASSWORD FOR LOGIN INTO INSTAGRAM
            enter_password = WebDriverWait(self.driver, timeOut).until(
                expected_conditions.presence_of_element_located((By.NAME, 'password')))
            enter_password.send_keys(password)
        
            # RETURNING THE PASSWORD and login into the account
            enter_password.send_keys(Keys.RETURN)

        except seExceptions.NoSuchElementException:
            #if cookies are enabled then this exception is expected
            if self.isUsingCookies:
                print('USING COOKIES!!!')
                return True
            else:
                print('LOGIN FAILURE. NoSuchElementException')
                return False
        except seExceptions.TimeoutException:
            #if cookies are enabled then this exception is expected
            if self.isUsingCookies:
                print('USING COOKIES!!!')
                return True
            else:
                print('LOGIN FAILURE. TimeOutException raised.')
                return False
        
        #handling popups
        if self.isUsingCookies:
            sleep(self.sleepDuration)
            #save login info popup - yes is clicked
            popup1 = self.wait.until(
                expected_conditions.presence_of_element_located(
                ("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')
                )).click()
            sleep(self.sleepDuration)
            
        else:
            #sleep to make look less bot like
            sleep(self.sleepDuration)
            #save login info popup - no is clicked
            popup1 = self.wait.until(
                expected_conditions.presence_of_element_located(
                ("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
                )).click()

            sleep(self.sleepDuration)

        #enable notifications popup - always no is clicked
        popup2 = self.wait.until(
            expected_conditions.presence_of_element_located(
            ("xpath", '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
            )).click()
        
        return True


    def findUser(self, user=None):
        if user == None:
            print('no user inputed') #maybe throw exception
            return

        #checks if user was previously searched for
        if user in self.CACHE:
            self.driver.get(self.CACHE[user])



        else:
            #redirects to dms
            self.driver.get(self.URLS['DirectMessageInbox'])
            

            #clicks on new message button
            newMessage = self.wait.until(
                expected_conditions.presence_of_element_located(
                ('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div')
                )).click()
            
            sleep(self.sleepDuration)
            
            #inputs username into search bar
            search = self.driver.switch_to.active_element
            search.send_keys(user)

            sleep(self.sleepDuration)
        
            # click on the username
            #self.driver.find_element("xpath",'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]').click()
            usernameResult = self.wait.until(
                expected_conditions.presence_of_element_located(
                ('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]')
                )).click()
            
            sleep(self.sleepDuration)
        
            # next button
            chatButton = self.wait.until(
                expected_conditions.presence_of_element_located(
                ('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')
                )).click()
            #adds user to cache for faster recall
            self.CACHE.update({user : self.driver.current_url})
        
        
        
    def sendMessage(self, message=None):
        if message == None or message == '':
            print('non valid message provided')
            return
        
        # locates message area
        messageBox = self.driver.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
    
        # types message
        messageBox.send_keys(message)
        sleep(self.sleepDuration)
    
        # send message
        messageBox.send_keys(Keys.RETURN)
    
    
