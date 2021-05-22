import os
import time
from twilio.rest import Client
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

def scrape():
    webpage = urlopen(req).read()
    page_soup = soup(webpage, 'html.parser')

    containers = page_soup.find('div',class_='statusmessage__content')
    if containers != None:
        old_text = containers.text
        return old_text
    else:
        return None

def main():
    i = 0
    while True:
        i += 1
        old_text = scrape()
        if old_text != None:
            time.sleep(30)
            new_text = scrape()

            if old_text != new_text:
                client.messages.create(
                    to='+46760471200',
                    from_='+12513094758',
                    body=new_text
                )
                break
            else:
                print(new_text)
                continue
        else:
            if i % 1000 == 0:
                print('Still None')
            continue
        
if __name__ == '__main__':
    account_sid = 'X'
    auth_token = 'X'

    client = Client(account_sid, auth_token)

    url = 'https://www.1177.se/Stockholm/sjukdomar--besvar/lungor-och-luftvagar/inflammation-och-infektion-ilungor-och-luftror/om-covid-19--coronavirus/om-vaccin-mot-covid-19/boka-tid-for-vaccination-mot-covid-19-i-stockholms-lan/'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    main()