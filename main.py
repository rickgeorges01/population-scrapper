import agregation

def main():
    # Appel et affichage de la population totale mondiale
    population_totale = agregation.obtenir_population_totale()
    print(f"Population totale mondiale : {population_totale}")

    # Appel et affichage de la densité moyenne de population
    densite_moyenne = agregation.obtenir_densite_population()
    print(f"Densité moyenne de population : {densite_moyenne}")

    # Appel et affichage du nombre total de pays
    nombre_de_pays = agregation.compter_nombre_de_pays()
    print(f"Nombre total de pays : {nombre_de_pays}")

    # Appel et affichage du pays avec la population maximale
    pays_population_max = agregation.obtenir_population_maximale()
    if pays_population_max:
        print(
            f"Pays avec la population maximale : {pays_population_max['Country']}, Population : {pays_population_max['Population']}")
    else:
        print("Impossible d'obtenir le pays avec la population maximale.")

    # Appel et affichage du pays avec la population minimale
    pays_population_min = agregation.obtenir_population_minimale()
    if pays_population_min:
        print(
            f"Pays avec la population maximale : {pays_population_min['Country']}, Population : {pays_population_min['Population']}")
    else:
        print("Impossible d'obtenir le pays avec la population minimale.")

    # Appel et affichage de la somme des migrations
    somme_migrations = agregation.somme_des_migrations()
    print(f"Somme nette des migrations : {somme_migrations}")

if __name__ == "__main__":
    main()
