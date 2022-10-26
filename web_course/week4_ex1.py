import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url  = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(0, count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    cnt = 0
    pos = 0
    for tag in tags:
        pos += 1
        if pos == position:
            print(f'Retrieved:{(str(tag.get("href",None)))}')
            url = str(tag.get('href', None))
            pos = 0
            break
