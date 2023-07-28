#import des librairies

from requests import get
from bs4 import BeautifulSoup
import csv 

def recupData(NumPage:int):
    """ Définition de l'URL avec variable du numero de page
    """

    LienScraping = "https://www.barreaudenice.com/annuaire/avocats/?fwp_paged="+str(NumPage)
    
    response = get(LienScraping)
    
    return response.content

def EnTeteCSV():
    """Ecriture de l'entete CSV
    """
    with open('Avocat.csv', 'w', newline='') as file :
        writer = csv.writer(file)
        hearders = ["NomPrenom", 'Adresse', "Telephone", "Mail"] # Définition de l'en tête
        writer.writerow(hearders)

def EcritureData(NomPrenom, Adresse, Telephone, Mail):
    """Fonction d'ecrire de données dans le fichier CSV afin de sauvegarder les données scrapé
    Args:
        NomPrenom
        Adresse
        Telephone
        Mail
    """
    with open ('Avocat.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            headers = [NomPrenom, Adresse, Telephone, Mail]
            writer.writerow(headers)
            file.close()

def Scrap():
    """
    Viens scraper la page avec les elements nom, adresse, telephone et mail
    Retourne Rien car ça ecrit directement dans le fichier CSV
    """
    
    EnTeteCSV()
    
    for i in range(1,50): # Scraping de 50 pages
        soup = BeautifulSoup(recupData(i), "html.parser")
        divSingle = soup.find_all('div', class_='callout secondary annuaire-single') # On vient prendre chaque div qui correspond à un avocat
                
        for info in divSingle:
            if info.find('h3').text != None: # Verification si l'élément n'est pas null
                avocatName = info.find('h3').text.strip() # On récupere le text de l'élément et on enleve les espaces et backspace inutile
            else:
                avocatName = "Introuvable"  # Si c'est Null, vient inscrire à la place "introuvable"
                
            if info.find("span", class_='adresse').text != None:
                adresse = info.find("span", class_='adresse').text.strip()
                adresse = " ".join(adresse.split()) # Vient rejoindre les backspace pour ne pas avoir de retour à la ligne
            else:
                adresse = "Introuvable"
            
            if info.find("span", class_='telephone').text != None:
                telephone = info.find("span", class_='telephone').text.strip()
                telephone = telephone.translate(str.maketrans('', '', 'T .')) # Enemeve le T et le .
            else:
                telephone = "Introuvable"
                
            SpanEmail = info.find("span", class_='email') # Ici on vient spécifier que l'on va taper dans une granularité plus fine avec le span email
            
            if SpanEmail != None:
                mail = SpanEmail.find("a").text.strip()
            else: 
                mail = "Introuvable"
            
            EcritureData(avocatName, adresse, telephone, mail) # Ecriture dans le fichier CSV

if __name__ == '__main__':
    Scrap()