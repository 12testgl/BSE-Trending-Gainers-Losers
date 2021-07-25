from bs4 import BeautifulSoup
import requests
import pprint


def bselosers():
    data = requests.get(
        'https://www.moneycontrol.com/stocks/marketstats/bseloser/index.php').text
    soup = BeautifulSoup(data, 'lxml')

    allCompanies = soup.find_all('span', class_='gld13 disin')

    companyNames = []
    for row in allCompanies:
        alink = row.find('a')
        companyNames.append(alink.text)

    tablerow = soup.find_all('tr')

    companyHigh = []
    companyLow = []
    companyClose = []
    companyChange = []
    companyLoss = []

    for tr in tablerow:
        high = tr.find_all('td', attrs={'width': 75, 'align': 'right'})

        for i in high:
            chigh = i.text.replace(',', '')
            companyHigh.append(chigh)
            break

        low = tr.find_all('td', attrs={'width': 80, 'align': 'right'})

        for i in low:
            clow = i.text.replace(',', '')
            companyLow.append(clow)
            break

        close = tr.find_all(
            'td', attrs={'width': 85, 'align': 'right'})

        for i in close:
            cclose = i.text.replace(',', '')
            companyClose.append(cclose)
            break

        change = tr.find_all(
            'td', attrs={'width': 45, 'align': 'right', "class": 'red'})
        if len(change) == 0:
            continue
        for i in change:

            cchange = i.text.replace(',', '')
            companyChange.append(cchange)
            break

        loss = tr.find_all(
            'td', attrs={'width': 45, 'align': 'right', "class": 'red'})
        if len(loss) == 0:
            continue

        companyLoss.append(float(loss[1].text.replace(',', '')))

    companyData = []

    for i in range(len(companyNames)):
        companyData.append({
            'company': companyNames[i],
            'High': float(companyHigh[i]),
            'Low': float(companyLow[i]),
            'Change': float(companyChange[i]),
            'Loss_in_per': float(companyLoss[i]),
            'close_price': float(companyClose[i])
        })

    new_dict = sorted(companyData, key=lambda i: i['Loss_in_per'])

    for i in range(len(new_dict)):

        pprint.pprint(new_dict[i])
        print(' ')



print('=====================Top Losers=====================')
bselosers()

