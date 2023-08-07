from chromeDriver import *
import re

class lyricFinder:
    def __init__(self) -> None:
        self.driver = initChromeDriver(headLess=True)

    def findLyrics(self, url=None):
        if url == None or len(url) == 0:
            print('No url provided')
            return None
        if not (re.match("https://https://www.azlyrics.com/", url) or re.match('https://www.azlyrics.com/', url)):
            print('Invalid url.\n Must match "https://www.azlyrics.com/"')
            return 
        
        self.driver.get(url)
        lyrics = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
            ('xpath','/html/body/div[2]/div[2]/div[2]/div[5]')))
        
        fileName = self.parseFileName(url)
        with open('./txt/' + fileName + '.txt','w') as f:
            f.write(lyrics.text)
        return True
    

    def parseFileName(self, url=None):
        url = re.sub('https://www.azlyrics.com/lyrics/', '', url)
        url = re.sub('.html', '', url)
        return  re.sub('/', '_', url)
    
    
        