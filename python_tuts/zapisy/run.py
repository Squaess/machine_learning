from bs4 import BeautifulSoup
import urllib.request

kod_grupy = ['v05-5N', 'v04-7G', 'v04-7C', 'v04-4N', 'v04-4K', 'v04-4C', 'v04-3N',
             'v04-3K', 'v04-2L', 'v04-1L', 'v03-4TS', 'v03-4K', 'v02-7C', 'v02-4C',
             'v02-3N', 'v02-3C', 'v02-1V1', 'v02-0V', 'v01-7G', 'v01-7G', 'v01-7C',
             'v01-4NL']

content = urllib.request.urlopen('http://akz.pwr.wroc.pl/katalog_zap.html').read()
soup = BeautifulSoup(content, features="html.parser")
table2 = soup.find(lambda tag: tag.name=='tbody')
for row in table2.findAll(lambda tag: tag.name == 'tr'):
    for column in row.findAll(lambda tag: tag.name == "td"):
        print(column.get_text())