import requests
from bs4 import BeautifulSoup

# URL of Delfi homepage
url = 'https://www.delfi.lt/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <h5> tags with class 'headline-title'
antrastes = soup.find_all('h5', class_='headline-title')

# Print each headline text
print("Delfi naujienų antraštės:")
for h5 in antrastes:
    nuoroda = h5.find('a')
    if nuoroda and nuoroda.get_text(strip=True):
        print("- " + nuoroda.get_text(strip=True))
