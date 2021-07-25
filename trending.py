from bs4 import BeautifulSoup
import requests
import pprint


def bsetrending():

    data = requests.get(
        'https://www.moneycontrol.com/stocks/marketstats/bsemact1/index.php').text

    soup = BeautifulSoup(data, 'lxml')

    allCompanies = soup.find_all('span', class_='gld13 disin')

    # print(allCompanies)

    companyNames = []
    for row in allCompanies:
        link = row.find('a').text
        companyNames.append(link)

    # print(companyNames)

    tablerow = soup.find_all('tr')

    companyHigh = []
    companyLow = []
    companyClose = []
    companyChange = []
    for tr in tablerow:

        # high price
        high = tr.find_all('td', attrs={'width': 175, 'align': 'right'})
        if len(high) == 0:
            continue
        for i in high:
            i = i.text.replace(',', '')
            companyHigh.append(float(i))
            break

        # low price
        low = tr.find_all('td', attrs={'width': 180, 'align': 'right'})

        for i in low:
            i = i.text.replace(',', '')
            companyLow.append(float(i))

        # close price

        close = tr.find_all('td', attrs={'width': 185, 'align': 'right'})

        # print(close)
        for i in close:
            i = i.text.replace(',', '')
            companyClose.append(i)

        change = tr.find_all('td', attrs={'width': 175, 'align': 'right'})
        # print(change)

        for i in change:
            if i.has_attr('class'):
                companyChange.append(float(i.text))

    companyData = []

    for i in range(len(companyNames)):
        companyData.append({
            'company': companyNames[i],
            'high': companyHigh[i],
            'low': companyLow[i],
            'change_in_per': companyChange[i],
            'close': companyClose[i]
        })

    new_dict = sorted(

        companyData, key=lambda i: i['change_in_per'], reverse=True
    )

    for i in range(len(new_dict)):
        pprint.pprint(new_dict[i])
        print(' ')


print('=====================Trending Stocks=====================')
bsetrending()
