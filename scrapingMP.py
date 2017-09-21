from bs4 import BeautifulSoup
from urllib.request import urlopen

list_of_mps = []

for count in range(1, 37):
    url = 'https://amarmp.com/mpsearch?division=0&district=0&thana=0&name=&page=' + str(count)
    content = urlopen(url)

    soup = BeautifulSoup(content, 'html.parser')

    name_box = soup.find_all('h3', attrs={'class': 'name'})
    constituency_box = soup.find_all('div', attrs={'class': 'mp-location'})
    party_box = soup.find_all('p', attrs={'class': 'party'})

    for i in range(len(name_box)):
        name = (name_box[i].text.split('-'))[0].strip()
        constituency = constituency_box[i].find('p').text.strip()
        party = party_box[i].text.strip()
        list_of_mps.append((name, constituency, party))


print(list_of_mps)
