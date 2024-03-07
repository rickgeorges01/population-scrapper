import agregation
import pandas as pd

def main():
    # Collecter les résultats des fonctions d'agrégation
    resultats = []

    population_totale = agregation.obtenir_population_totale()
    print(f"Population totale mondiale : {population_totale}")
    resultats.append({"Statistique": "Population Totale", "Valeur": population_totale})

    densite_moyenne = agregation.obtenir_densite_population()
    print(f"Densité moyenne de population : {densite_moyenne}")
    resultats.append({"Statistique": "Densité Moyenne", "Valeur": densite_moyenne})

    nombre_de_pays = agregation.compter_nombre_de_pays()
    print(f"Nombre total de pays : {nombre_de_pays}")
    resultats.append({"Statistique": "Nombre Total de Pays", "Valeur": nombre_de_pays})

    pays_population_max = agregation.obtenir_population_maximale()
    if pays_population_max:
        print(f"Pays avec la population maximale : {pays_population_max['Country']}, Population : {pays_population_max['Population']}")
        resultats.append({"Statistique": "Pays avec Population Maximale", "Valeur": f"{pays_population_max['Country']}, {pays_population_max['Population']}"})
    else:
        print("Impossible d'obtenir le pays avec la population maximale.")

    pays_population_min = agregation.obtenir_population_minimale()
    if pays_population_min:
        print(f"Pays avec la population minimale : {pays_population_min['Country']}, Population : {pays_population_min['Population']}")
        resultats.append({"Statistique": "Pays avec Population Minimale", "Valeur": f"{pays_population_min['Country']}, {pays_population_min['Population']}"})
    else:
        print("Impossible d'obtenir le pays avec la population minimale.")

    somme_migrations = agregation.somme_des_migrations()
    print(f"Somme nette des migrations : {somme_migrations}")
    resultats.append({"Statistique": "Somme des Migrations", "Valeur": somme_migrations})

    # Convertir la liste de dictionnaires en DataFrame pandas
    resultats_df = pd.DataFrame(resultats)

    # Sauvegarder le DataFrame dans un fichier CSV
    resultats_df.to_csv('resultats_agregation.csv', index=False)

    # Afficher un message pour confirmer la sauvegarde
    print("Les résultats d'agrégation ont été sauvegardés dans 'resultats_agregation.csv'.")

if __name__ == "__main__":
    main()
