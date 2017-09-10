# Library Booker 
# pesutsinga 2017

USERNAME = ''
PASSWORD = ''

#either 'Facility' or 'PC'
BOOKING_MODE = "PC"
from splinter import Browser
chrome = Browser('chrome')
def timeDelay(time):
    chrome.is_element_present_by_name('!@#$%^^%$#@!', wait_time=time)

def login_ntupcb():

    url = 'http://gg.gg/libbook'
    chrome.visit(url)
    chrome.fill('Username', USERNAME)
    chrome.fill('Password', PASSWORD)
 
   # Find and click the 'search' button
    button = chrome.find_by_tag('button')
    # Interact with elements
    button.click()

def main():
    login_ntupcb()
    if BOOKING_MODE == 'PC':
        button = chrome.find_by_id('tdPcBook')
        button.click()
        with chrome.get_iframe('frmAdminViewControls') as iframe:
            iframe.find_by_id('pnlInsLoc3').click()
            iframe.find_by_id('pnlInsPcGrp0').click()
        for value in [31, 26, 7, 27]:
            chrome.select('drplistpcgrp', value)
            timeDelay(0.1);
            with chrome.get_iframe('frmSeating') as iframe:
                print(iframe.html)

if __name__ == '__main__':
    main()
