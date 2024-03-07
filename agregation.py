import db
def obtenir_population_totale():
    '------------------------CALCULE ET RETOURNE LA POPULATION MONDIALE------------------------'
    connection = db.connect_to_database()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT SUM(population) AS PopulationTotale FROM population_data;")
            resultat = cursor.fetchone()
            # retourne le resultat totale
            return resultat[0]
    except db.mysql.connector.Error as e:
        print(f"Erreur lors de l'agrégation des données (Population mondiale): {e}")
    finally:
        if connection.is_connected():
            connection.close()


def obtenir_densite_population():
    '------------------CALCUL ET RETOURNE LA DENSITE MOYENNE DE POPULATION----------------------'
    connection = db.connect_to_database()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT AVG(Density) AS DensiteMoyenne FROM population_data;")
            resultat = cursor.fetchone()
            # Retourne la densité moyenne
            return resultat[0]
    except db.mysql.connector.Error as e:
        print(f"Erreur lors de l'agrégation des données (Densité Moyenne): {e}")
    finally:
        if connection.is_connected():
            connection.close()


def compter_nombre_de_pays():
    '------------------COMPTE ET RETOURNE LE NOMBRE DE PAYS-----------------'
    connection = db.connect_to_database()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM population_data;")
            resultat = cursor.fetchone()
            # Retourne le nombre de pays
            return resultat[0]
    except db.mysql.connector.Error as e:
        print(f"Erreur lors de l'agrégation des données (Nombre de Pays): {e}")
    finally:
        connection.close()


def obtenir_population_maximale():
    '------------TROUVE LE PAYS AVEC UNE POPULATION MAXIMALE ET RETOURNE LE PAYS ET SA POPULATION MAXIMALE---------'
    connection = db.connect_to_database()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT Country, MAX(Population) FROM population_data;")
            resultat = cursor.fetchone()
            # Retourne le pays max et sa population
            return {"Country": resultat[0], "Population": resultat[1]}
    except db.mysql.connector.Error as e:
        print(f"Erreur lors de l'agrégation des données (Pays max et sa population): {e}")
    finally:
        connection.close()


def obtenir_population_minimale():
    '----------------TROUVE LE PAYS AVEC LA POPULATION MINIMALE ET RETOURNE CE PAYS ET SA POPULATION------------------'
    connection = db.connect_to_database()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT Country, MIN(Population) FROM population_data WHERE Population > 0;")
            resultat = cursor.fetchone()
            # Retourne le pays min et sa population
            return {"Country": resultat[0], "Population": resultat[1]}
    except db.mysql.connector.Error as e:
        print(f"Erreur lors de l'agrégation des données (Pays min et sa population): {e}")
    finally:
        if connection.is_connected():
            connection.close()


def somme_des_migrations():
    '-------------------CALCULE ET RETOURNE LA SOMME NETTE DES MIGRATIONS-------------------'
    connection = db.connect_to_database()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT SUM(Migrants) FROM population_data WHERE Migrants IS NOT NULL;")
            resultat = cursor.fetchone()
            # Retourne la somme des migrations
            return resultat[0]
    except db.mysql.connector.Error as e:
        print(f"Erreur lors de l'agrégation des données (migrations): {e}")
    finally:
        if connection.is_connected():
            connection.close()
