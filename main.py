import agregation
import pandas as pd

def main():
    # Collecter les résultats des fonctions d'agrégation
    resultats = []

    # Population totale mondiale
    population_totale = agregation.obtenir_population_totale()["Population totale mondiale"]
    print(f"La population totale mondiale est de : {population_totale} habitants.")
    resultats.append({"Statistique": "Population mondiale totale", "Valeur": f"{population_totale} habitants"})

    # Densité moyenne de la population
    densite_moyenne = agregation.obtenir_densite_population()["Densité Moyenne de la population"]
    print(f"La densité moyenne de la population mondiale est de : {densite_moyenne} habitants par km².")
    resultats.append({"Statistique": "Densité moyenne de population", "Valeur": f"{densite_moyenne} hab/km²"})

    # Nombre total de pays
    nombre_de_pays = agregation.compter_nombre_de_pays()["Nombre totale de pays"]
    print(f"Le nombre total de pays répertoriés est de : {nombre_de_pays}.")
    resultats.append({"Statistique": "Nombre total de pays", "Valeur": f"{nombre_de_pays} pays"})

    # Pays avec la population maximale
    pays_population_max = agregation.obtenir_population_maximale()
    max_country = pays_population_max['Country']
    max_population = pays_population_max['Population']
    print(f"Le pays avec la plus grande population est {max_country}, avec {max_population} habitants.")
    resultats.append({"Statistique": "Pays avec la plus grande population", "Valeur": f"{max_country}: {max_population} habitants"})

    # Pays avec la population minimale (non nulle)
    pays_population_min = agregation.obtenir_population_minimale()
    min_country = pays_population_min['Country']
    min_population = pays_population_min['Population']
    print(f"Le pays avec la plus petite population (non nulle) est {min_country}, avec {min_population} habitants.")
    resultats.append({"Statistique": "Pays avec la plus petite population (non nulle)", "Valeur": f"{min_country}: {min_population} habitants"})

    # Somme des migrations nettes
    somme_migrations = agregation.somme_des_migrations()["Sommes des migrations"]
    print(f"La somme nette des migrations est de : {somme_migrations}.")
    resultats.append({"Statistique": "Somme nette des migrations", "Valeur": f"{somme_migrations}"})

    # Convertir la liste de dictionnaires en DataFrame pandas et sauvegarder dans un fichier CSV
    resultats_df = pd.DataFrame(resultats)
    resultats_df.to_csv('resultats_agregation.csv', index=False)

    print("Les résultats d'agrégation ont été sauvegardés avec succès dans le fichier 'resultats_agregation.csv'.")

if __name__ == "__main__":
    main()
