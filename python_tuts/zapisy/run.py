from bs4 import BeautifulSoup
import urllib.request

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

kod_grupy = ['v05-5N', 'v04-7G', 'v04-7C', 'v04-4N', 'v04-4K', 'v04-4C', 'v04-3N',
             'v04-3K', 'v04-2L', 'v04-1L', 'v03-4TS', 'v03-4K', 'v02-7C', 'v02-4C',
             'v02-3N', 'v02-3C', 'v02-1V1', 'v02-0V', 'v01-7G', 'v01-7G', 'v01-7C',
             'v01-4NL']

content = urllib.request.urlopen('http://akz.pwr.wroc.pl/katalog_zap.html').read()
soup = BeautifulSoup(content, features="html.parser")
table2 = soup.find(lambda tag: tag.name=='tbody')
if table2 == None:
    raise ConnectionError()

for row in table2.findAll(lambda tag: tag.name == 'tr'):
    content = row.get_text()
    splited = content.split()
    if splited[1] in kod_grupy and splited[5] != '0':
        splited_n = content.split('\n')
        splited_n[4] = bcolors.WARNING + splited_n[4] + bcolors.ENDC
        splited_n[6] = bcolors.FAIL + splited_n[6] + bcolors.ENDC
        to_print = "\n".join(splited_n)
        print(to_print)
    
    # for column in row.findAll(lambda tag: tag.name == "td"):
    #     print(column.get_text())