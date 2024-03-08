import db
def obtenir_population_totale():
    # ------------------------CALCULE ET RETOURNE LA POPULATION MONDIALE------------------------
    connection = db.connect_to_database()
    try:
        with connection.cursor() as cursor:
            # Exécution de la requête pour obtenir la somme de la population
            cursor.execute("SELECT SUM(population) AS PopulationTotale FROM population_data;")
            resultat = cursor.fetchone()

            # Insertion du résultat dans la table des résultats d'agrégation
            cursor.execute("INSERT INTO resultats_agregation (statistique, valeur) VALUES (%s, %s)",
                           ("Population totale mondiale", str(resultat[0])))
            connection.commit()

            # Retourne le résultat total
            return {"Population totale mondiale": resultat[0]}
    except db.mysql.connector.Error as e:
        print(f"Erreur lors de l'agrégation des données (Population mondiale): {e}")
    finally:
        if connection.is_connected():
            connection.close()


def obtenir_densite_population():
    # ------------------CALCUL ET RETOURNE LA DENSITE MOYENNE DE POPULATION----------------------
    connection = db.connect_to_database()
    try:
        with connection.cursor() as cursor:
            # Exécution de la requête pour obtenir la densité moyenne
            cursor.execute("SELECT AVG(Density) AS DensiteMoyenne FROM population_data;")
            resultat = cursor.fetchone()

            # Insertion du résultat dans la table des résultats d'agrégation
            cursor.execute("INSERT INTO resultats_agregation (statistique, valeur) VALUES (%s, %s)",
                           ("Densité moyenne de population", str(resultat[0])))
            connection.commit()

            # Retourne la densité moyenne
            return {"Densité Moyenne de la population": resultat[0]}
    except db.mysql.connector.Error as e:
        print(f"Erreur lors de l'agrégation des données (Densité Moyenne): {e}")
    finally:
        if connection.is_connected():
            connection.close()


def compter_nombre_de_pays():
    # ------------------COMPTE ET RETOURNE LE NOMBRE DE PAYS-----------------
    connection = db.connect_to_database()
    try:
        with connection.cursor() as cursor:
            # Exécution de la requête pour compter le nombre de pays
            cursor.execute("SELECT COUNT(*) FROM population_data;")
            resultat = cursor.fetchone()

            # Insertion du résultat dans la table des résultats d'agrégation
            cursor.execute("INSERT INTO resultats_agregation (statistique, valeur) VALUES (%s, %s)",
                           ("Nombre total de pays", str(resultat[0])))
            connection.commit()

            # Retourne le nombre de pays
            return {"Nombre totale de pays": resultat[0]}
    except db.mysql.connector.Error as e:
        print(f"Erreur lors de l'agrégation des données (Nombre de Pays): {e}")
    finally:
        connection.close()


def obtenir_population_maximale():
    # ------------TROUVE LE PAYS AVEC UNE POPULATION MAXIMALE ET RETOURNE LE PAYS ET SA POPULATION MAXIMALE---------
    connection = db.connect_to_database()
    try:
        with connection.cursor() as cursor:
            # Exécution de la requête pour trouver le pays avec la population maximale
            cursor.execute("SELECT Country, MAX(Population) FROM population_data;")
            resultat = cursor.fetchone()

            # Insertion du résultat dans la table des résultats d'agrégation
            cursor.execute("INSERT INTO resultats_agregation (statistique, valeur) VALUES (%s, %s)",
                           ("Pays avec population maximale", f"{resultat[0]}: {resultat[1]}"))
            connection.commit()

            # Retourne le pays max et sa population
            return {"Country": resultat[0], "Population": resultat[1]}
    except db.mysql.connector.Error as e:
        print(f"Erreur lors de l'agrégation des données (Pays max et sa population): {e}")
    finally:
        connection.close()


def obtenir_population_minimale():
    # ----------------TROUVE LE PAYS AVEC LA POPULATION MINIMALE ET RETOURNE CE PAYS ET SA POPULATION------------------
    connection = db.connect_to_database()
    try:
        with connection.cursor() as cursor:
            # Exécution de la requête
            cursor.execute("SELECT Country, MIN(Population) FROM population_data WHERE Population > 0;")
            resultat = cursor.fetchone()

            # Insertion du résultat dans la table des résultats d'agrégation
            cursor.execute("INSERT INTO resultats_agregation (statistique, valeur) VALUES (%s, %s)",
                           ("Pays avec population minimale", f"{resultat[0]}: {resultat[1]}"))
            connection.commit()
            # Retourne le pays min et sa population
            return {"Country": resultat[0], "Population": resultat[1]}

    except db.mysql.connector.Error as e:
        print(f"Erreur lors de l'agrégation des données (Pays min et sa population): {e}")
    finally:
        if connection.is_connected():
            connection.close()


def somme_des_migrations():
    # -------------------CALCULE ET RETOURNE LA SOMME NETTE DES MIGRATIONS-------------------
    connection = db.connect_to_database()
    try:
        with connection.cursor() as cursor:
            # Exécution de la requête pour obtenir la somme des migrations
            cursor.execute("SELECT SUM(Migrants) FROM population_data WHERE Migrants IS NOT NULL;")
            resultat = cursor.fetchone()
            # Insertion du résultat dans la table des résultats d'agrégation
            cursor.execute("INSERT INTO resultats_agregation (statistique, valeur) VALUES (%s, %s)",
                           ("Somme des migrations", str(resultat[0])))
            connection.commit()

            # Retourne la somme des migrations
            return {"Somme des migrations": resultat[0]}
    except db.mysql.connector.Error as e:
        print(f"Erreur lors de l'agrégation des données (migrations): {e}")
    finally:
        if connection.is_connected():
            connection.close()
