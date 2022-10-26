import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Get SSL Certification Error handeling
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Data Collect From the Website
link = input('Enter url of the website:  ')
html = urllib.request.urlopen(link, context = ctx).read()

tree = ET.fromstring(html)
lst = tree.findall('comments/comment')
print(f'Comments count: {len(lst)}')

answer = []
for item in lst:
    count = item.find('count').text
    answer.append(int(count))

print(f'The sum is equal to: {sum(answer)}')