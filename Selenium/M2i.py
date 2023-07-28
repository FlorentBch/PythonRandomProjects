from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime
#from time import gmtime, strftime
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.keys import Keys

#Pour garder la fenêtre ouverte, plus necessaire lors de l'automatisation 
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.maximize_window() # Pour ouvir la fentre chrome en grand
driver.get("https://sign.m2iformation.fr/signin") # Connexion au site M2i

driver.find_element(By.XPATH,'//*[@id="inputPhoneNumber"]').click()
driver.find_element(By.XPATH,'//*[@id="inputPhoneNumber"]').send_keys('florent.buchet@labom2iformation.fr') # Ajout du champ ID

driver.find_element(By.XPATH,'//*[@id="inputSmsCode"]').click()
driver.find_element(By.XPATH,'//*[@id="inputSmsCode"]').send_keys('72153') # Ajout du code

driver.find_element(By.XPATH,'//*[@id="connexion"]').click() # On clique sur la connexion


driver.implicitly_wait(10)  # On attends 10 secondes afin d'être sur de gérer la latence 

driver.find_element(By.XPATH,'/html/body/header/div[2]/div/div/div/div/nav/ul/li[2]/a').click() # On clique sur l'onglet fiche de présence

ListeDate = []
ids = driver.find_elements(By.XPATH,'//*[@id]') # On prends tous les valeurs des ID de la page commencant par un XPATH égal à par exemple : //*[@id="05/15/2023pm"]
for ii in ids:
    ListeDate.append(ii.get_attribute('id')) # On ajoute tous les id des éléments precedemment récuperé

DateTime = datetime.now() #Date actuel sous format avec date et heure
FormatDateTime = (f'{DateTime:%m/%d/%Y%p}').lower() # Ici on reformate le dateTime en MM/DD/YYYY/am ou pm. Le tout en minuscule

for DateActuel in ListeDate:
    if DateActuel == FormatDateTime: 
        driver.find_element(By.XPATH,'//*[@id="'+DateActuel+'"]').click() # On clique sur la case du jour et de la temporalité
        print(FormatDateTime , DateActuel)

driver.quit()