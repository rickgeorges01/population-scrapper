from fastapi import FastAPI
import agregation

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "Bienvenue RTIT Consulting": "Bienvenue dans l'API de Démographie Mondiale",
        "Description": "Cette API fournit un accès programmable à des données démographiques agrégées, offrant des aperçus sur la population mondiale, la densité, la croissance démographique, et plus encore.",
        "Instructions": "Utilisez les endpoints fournis pour explorer diverses statistiques démographiques.",
        "Endpoints": {
            "/population-totale": "Obtenez la population totale mondiale.",
            "/densite-moyenne": "Découvrez la densité moyenne de population.",
            "/nombre-de-pays": "Comptez le nombre total de pays répertoriés.",
            "/population-maximale": "Identifiez le pays avec la plus grande population.",
            "/population-minimale": "Trouvez le pays avec la plus petite population (non nulle).",
            "/somme-migrations": "Examinez la somme nette des migrations."
        },
        "Avertissement": "Ces données sont agrégées à des fins d'analyse et ne doivent pas être utilisées pour des décisions critiques sans vérification."
    }


@app.get("/population-totale")
def read_population_totale():
    return agregation.obtenir_population_totale()

@app.get("/densite-moyenne")
def read_densite_moyenne():
    return agregation.obtenir_densite_population()

@app.get("/nombre-de-pays")
def read_nombre_de_pays():
    return agregation.compter_nombre_de_pays()

@app.get("/population-maximale")
def read_population_maximale():
    return agregation.obtenir_population_maximale()

@app.get("/population-minimale")
def read_population_minimale():
    return agregation.obtenir_population_minimale()

@app.get("/somme-migrations")
def read_somme_migrations():
    return agregation.somme_des_migrations()
