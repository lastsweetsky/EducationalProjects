import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

#Get SSL Certification Error handeling
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Data Collect From the Website
link = input('Enter url of the website:  ')
to_find = input('Enter what you are looking for: ')
html = urllib.request.urlopen(link, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    content = tag.get('url',None)
    if content == to_find:
        print('\nYour link is present!')
        break
else:
    print('\nYour link in not presented!')

print('\nThe scan is over!')
