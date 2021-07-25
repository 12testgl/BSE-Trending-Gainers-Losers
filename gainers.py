from bs4 import BeautifulSoup
import requests
import pprint


def bsegainers():
    data = requests.get(
        'https://www.moneycontrol.com/stocks/marketstats/bsegainer/index.php').text

    soup = BeautifulSoup(data, 'lxml')

    # company names

    allCompanies = soup.find_all('span', class_='gld13 disin')

    companyNames = []

    for i in allCompanies:
        a = i.find('a')
        companyNames.append(a.text)

    # high
    tablerow = soup.find_all('tr')
    companyHigh = []
    companyLow = []
    companyClose = []
    companyGain = []
    companyChange = []

    for tr in tablerow:
        high = tr.find_all('td', attrs={'width': 75, 'align': 'right'})

        for i in high:
            i = i.text.replace(',', '')
            companyHigh.append(float(i))

    # low

        low = tr.find_all('td', attrs={'width': 80, 'align': 'right'})

        for i in low:
            i = i.text.replace(',', '')
            companyLow.append(float(i))
            break
    # close or last price
        close = tr.find_all('td', attrs={'width': 85, 'align': 'right'})

        for i in close:
            i = i.text.replace(',', '')
            companyClose.append(float(i))
            break
    # gain
        gain = tr.find_all(
            'td', attrs={'width': 45, 'align': 'right', 'class': 'green'})
        if len(gain) == 0:
            continue
        companyGain.append(float(gain[0].text))
    # change
        change = tr.find_all(
            'td', attrs={'width': 55, 'align': 'right', 'class': 'green'})
        if len(change) == 0:
            continue
        companyChange.append(float(change[0].text))

    companyData = []

    for i in range(len(companyNames)):
        companyData.append({
            'company': companyNames[i],
            'high': companyHigh[i],
            'low': companyLow[i],
            'change': companyChange[i],
            'gain_in_per': companyGain[i],
            'close_in_per': companyClose[i]
        })

    for i in range(len(companyNames)):
        pprint.pprint(companyData[i])
        print(' ')


print('=====================Top Gainers=====================')
bsegainers()
