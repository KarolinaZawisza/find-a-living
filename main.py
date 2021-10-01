import requests as requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

url ='https://www.zillow.com/orlando-fl/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Orlando%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.78894445133962%2C%22east%22%3A-80.84412023258962%2C%22south%22%3A28.02270944048895%2C%22north%22%3A28.822234426011068%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A13121%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A576423%2C%22max%22%3A1235192%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A1400%2C%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
response = requests.get(url, headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

results_links = [f'https://www.zillow.com{link["href"]}' if 'http' not in link['href'] else link['href'] for link in soup.select('.list-card-top a')]
results_addresses = [address.get_text() for address in soup.select('.list-card-addr')]
results_prices = [price.get_text() for price in soup.select('.list-card-price')]



