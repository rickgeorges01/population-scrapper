import requests
import pandas as pd
from bs4 import BeautifulSoup
import db

# Fonction pour insérer les données à partir du CSV dans la base de données
def insert_data_from_csv_to_db(csv_file_path):
    data_df = pd.read_csv(csv_file_path)
    data_df.fillna(0, inplace=True)
    print(data_df.head())
    connection = db.connect_to_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            for index, row in data_df.iterrows():
                print(f"Insertion de la ligne {index} : {row['Country']}")
                query = ("INSERT INTO population_data "
                         "(Country, Population, `Net Change`, `Yearly Change`, Density, `Land Area`, Migrants, `Fertility Rate`, `Median Age`, `Urban Population`, `World Share`) "
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                values = (row['Country'], row['Population'], row['Net Change'], row['Yearly Change'],
                          row['Density'], row['Land Area'], row['Migrants'], row['Fertility Rate'],
                          row['Median Age'], row['Urban Population'], row['World Share'])
                cursor.execute(query, values)
            connection.commit()
            print(f"{cursor.rowcount} lignes insérées.")
        except db.mysql.connector.Error as e:
            print(f"Erreur lors de l'insertion des données: {e}")
        finally:
            cursor.close()
            connection.close()
            print("Connexion MySQL est fermée")


# URL du site Worldometer (Population par pays)
url = 'https://www.worldometers.info/world-population/population-by-country/'
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Récupération du contenu de la page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Recherche des données
table = soup.find('table', id='example2')
rows = table.find_all('tr')

# Initialisation d'une liste vide pour stocker les données de chaque pays
data = []

# Itération sur chaque ligne de la table HTML
for row in rows[1:]:
    # Récupération de toutes les cellules (colonnes) de la ligne courante
    cols = row.find_all('td')

    # Extraction et nettoyage des données de chaque colonne nécessaire
    country = cols[1].text.strip()
    population = cols[2].text.strip().replace(',', '')
    net_change = cols[3].text.strip().replace(',', '')
    yearly_change = cols[4].text.strip()
    density = cols[5].text.strip().replace(',', '')
    land_area = cols[6].text.strip().replace(',', '')
    migrants = cols[7].text.strip().replace(',', '')
    fert_rate = cols[8].text.strip()
    med_age = cols[9].text.strip()
    urban_pop = cols[10].text.strip()
    world_share = cols[11].text.strip()

    # Ajout des données extraites dans la liste 'data' sous forme de dictionnaire
    data.append({
        'Country': country,
        'Population': population,
        'Net Change': net_change,
        'Yearly Change': yearly_change,
        'Density': density,
        'Land Area': land_area,
        'Migrants': migrants,
        'Fertility Rate': fert_rate,
        'Median Age': med_age,
        'Urban Population': urban_pop,
        'World Share': world_share
    })

#Création d'un DataFrame à partir d'une liste de dictionnaire
df = pd.DataFrame(data)

# Après avoir sauvé les données dans le CSV
df.to_csv('world_population_data.csv', index=False)

# Déclaration de la variable csv_file_path
csv_file_path = 'world_population_data.csv'


# Appeler la fonction pour insérer les données du CSV dans la base de données
insert_data_from_csv_to_db('world_population_data.csv')
