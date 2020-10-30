# Importamos las librerias que vamos a utilizar.
import requests
from requests import get
import beautifulsoup4 as bs4
import pandas as pd
import numpy as np

# Variables
url = 'https://www.imdb.com/search/title/?groups=top_1000'
headers = {"Accept-Language": "en-US, en;q=0.5"}
results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")

# Inicializar el almacenamiento de datos
titles = []
years = []
time = []
imdb_rating = []
metascores = []
votes = []
us_gross = []

# Anidamos el scrap
movie_div = soup.find_all('div', class_='lister-item mode-advanced')

# Bucle FOR para recorrer todo el sitio.
for container in movie_div:
    
