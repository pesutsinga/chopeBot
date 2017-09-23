# Library Booker
# pesutsinga 2017
from splinter import Browser

USERNAME = ''
PASSWORD = ''
# either 'Facility' or 'PC'
BOOKING_MODE = 'PC'
chrome = Browser('chrome')


def timeDelay(time):
    chrome.is_element_present_by_name('!@#$%^&*())(*&^%$#@!', wait_time=time)


def login_ntupcb():

    url = 'http://gg.gg/libbook'
    chrome.visit(url)
    chrome.fill('Username', USERNAME)
    chrome.fill('Password', PASSWORD)
    # Find and click the 'search' button
    button = chrome.find_by_tag('button')
    # Interact with elements
    button.click()


def scrape_pc():
    if BOOKING_MODE == 'PC':
        button = chrome.find_by_id('tdPcBook')
        button.click()
        with chrome.get_iframe('frmAdminViewControls') as iframe:
            iframe.find_by_id('pnlInsLoc3').click()
            iframe.find_by_id('pnlInsPcGrp0').click()
        for value in [31, 26, 7, 27]:
            url = 'https://ntupcb.ntu.edu.sg/fbscbs/PCBooking/\
                SeatingParentForm.aspx?LocId=2&PcGrpId=' + str(value)
            chrome.visit(url)
            with chrome.get_iframe('frmSeating') as iframe:
                tables = iframe.find_by_css('.ItemStyleProp')
                for table in hooray:
                    if table.find_by_tag('img'):
                        if table.text != '':
                            print(">>>")
                            print(table.text)


def main():
    login_ntupcb()
    scrape_pc()

if __name__ == '__main__':
    main()
