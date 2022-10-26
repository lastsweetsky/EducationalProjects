import ssl
import urllib.error
import urllib.request

from datetime import datetime

import pandas as pd
from bs4 import BeautifulSoup

'''Receive url of website '''


def getData():
    link = input('Enter url of the website:  ')
    return link


'''Get SSL Certification Error handling'''


def getSSLcertError():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


'''Data Collect From the Website'''


def dataCollection(link, ctx):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


'''Find if the url contains on the website.
You must change "href" to your format of the website'''


def findIntersection(soup, to_find):
    tags = soup('a')
    for tag in tags:
        content = tag.get('href', None)
        if content == to_find:
            print('\nYour link is presented')
            return 'Positive'
    else:
        print('\nYour link is not presented!')
        return 'Negative'


def main():
    to_find = input('Enter what you are looking for: ')

    df = pd.DataFrame(data = {'Searched_in': [],
          'Searched': [],
          'Status': [],
          'Date': []})

    while True:
        link = getData()
        ctx = getSSLcertError()
        soup = dataCollection(link=link, ctx=ctx)
        status = findIntersection(to_find=to_find, soup=soup)

        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")

        df.loc[len(df)]=[link,to_find,status,date]
        if input('Want to continue? Press Enter to continue: ' ) != '':
            break

    sheet_name = now.strftime("%b-%d-%Y")
    with pd.ExcelWriter("C:\\Users\\WSA\\Desktop\\results.xlsx") as writer:
        df.to_excel(writer, sheet_name=sheet_name,index=False)


if __name__ == '__main__':
    main()

# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Aniqa.html
# http://py4e-data.dr-chuck.net/known_by_Kiarash.html
# http://py4e-data.dr-chuck.net/known_by_Anona.html


