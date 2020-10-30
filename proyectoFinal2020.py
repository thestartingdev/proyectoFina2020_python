# Importamos las librerias que vamos a utilizar.
import requests
from requests import get
from bs4 import BeautifulSoup
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
imdb_ratings = []
metascores = []
votes = []
us_gross = []

# Anidamos el scrap
movie_div = soup.find_all('div', class_='lister-item mode-advanced')

# Bucle FOR para recorrer todo el sitio.
for container in movie_div:
    # Nombre
    name = container.h3.a.text
    titles.append(name)

    # Año
    year = container.h3.find('span', class_='lister-item-year')
    years.append(year)

    # Duracion de la pelicula
    runtime = container.p.find('span', class_='runtime').text if container.p.find('span', class_='runtime').text else '-'
    time.append(runtime)

    # IMDB Rating
    rating = float(container.strong.text)
    imdb_ratings.append(rating)

print(titles)
print(years)
print(time)
print(imdb_ratings)
