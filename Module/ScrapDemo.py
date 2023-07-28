#import de mes librairies

from dotenv import load_dotenv
import os
from requests import get
from bs4 import BeautifulSoup
import csv 
def chargementEnv(VARENV:str):
    """Méthode qui permet de charger une variable d'environnement à partir d'un fichier .env

    Args:
        VARENV (str): Le nom de la variable à changer

    Returns:
        _type_: Valeur de la variable
    """
    load_dotenv()
    return os.getenv(VARENV)

def recupData():
    """Méthode démo pour get data d'un site
    """

    bookscrap = chargementEnv("BOOKSCRAP")
    url = bookscrap + 'catalogue/page-1.html'
    
    response = get(url)
    return response.content

def scrapBs():
    ma_page = recupData()
    soup = BeautifulSoup(ma_page, "html.parser")
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')
    print(articles)
    
    with open('saved_data.csv', 'w', newline='') as file :
        writer = csv.writer(file)
        hearders = ["Titre", 'Note', "Prix"]
        writer.writerow(hearders)
        
    for article in articles:
        # Titre
        image = article.find("img")
        title = image.attrs['alt']
        print("Titre : ", title)
        
        # Notes
        star = article.find('p')
        star = star ['class'][1]
        print("notes du livre :", star,"sur 5")
        
        # Prix
        price = article.find('p', class_='price_color').text
        print("Prix (en {}) du livre: {}".format(price[:1],price[1:]))
            
        with open ('saved_data.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            hearders = [title, star, price[1:]]
            writer.writerow(hearders)

if __name__ == '__main__':
    scrapBs()
