# Importing libraries
import urllib.request
from bs4 import BeautifulSoup

uh = urllib.request.urlopen('https://www.tradingview.com/symbols/EURUSD/ideas/?sort=recent').read()
data = uh.decode()
soup = BeautifulSoup(data, 'html.parser')

# Variables
short_list = list()
long_list = list()

all_span_tags = soup.find_all('span')

# Loop through all span tags to check for long and short
for i in all_span_tags:
    if 'Short' not in i:
        if 'Long' in i:
            long_list.append(i.contents)
    else:
        short_list.append(i.contents)

# Print the number of long and shorts
print('Shorts : ', len(short_list), '######', 'Longs : ', len(long_list))

