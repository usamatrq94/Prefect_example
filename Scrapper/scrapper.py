import requests
from bs4 import BeautifulSoup
import pandas as pd

def top_gainers_today():
    # coin martket cap for top gainers and loser, updated everyday
    URL = "https://coinmarketcap.com/gainers-losers/"

    # using request to fetch html
    r = requests.get(URL)

    # making a Soup object and finding the top gainers table
    soup = BeautifulSoup(r.content, 'html5lib')
    gainers_table = soup.find('div', class_ = 'h7vnx2-1 gDdiUn').find('tbody')
    
    # scrapping symbol, prince, percentage gain and volume
    gainers = []
    for crypto in gainers_table.findAll('tr'):
        symbol = crypto.find('p', class_='sc-1eb5slv-0 gGIpIK coin-item-symbol').text
        price = crypto.find('span').text[1:]
        gain = crypto.find('span', class_='sc-15yy2pl-0 kAXKAX').text[:-1]
        volume = crypto.findAll('td', style='text-align:right')[-1].text[1:]
        gainers.append([symbol, price, gain, volume])
        
    # creating and returning Dataframe    
    top_gainers = pd.DataFrame(gainers, columns = ['Symbol', 'Price', 'Gain_Percentage', 'Volume'])
    return top_gainers


print(top_gainers_today())