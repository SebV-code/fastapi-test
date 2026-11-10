# IBM HR Data Explorer API

API pédagogique développée avec FastAPI pour tester le déploiement d'une application Python sur VPS et explorer plusieurs opérations Pandas sur un jeu de données RH fictif d'IBM.

!!! Le serveur n'est pas toujours en ligne si vous souhaitez effectuer un test merci de contacter le propriétaire du repo !!!

## Démonstration

- [Tester l'API](https://portfolio.vatinel.fr/fastapi-test/)
- [Documentation Swagger](https://portfolio.vatinel.fr/fastapi-test/docs)
- [Documentation ReDoc](https://portfolio.vatinel.fr/fastapi-test/redoc)

## Fonctionnalités

L'API permet de :

- prévisualiser les premières lignes du jeu de données ;
- afficher les valeurs uniques d'une colonne ;
- regrouper et agréger les données ;
- filtrer les lignes selon une ou plusieurs catégories ;
- sélectionner les valeurs situées dans un quantile.

## Routes disponibles

- `GET /` : informations générales ;
- `GET /preview` : aperçu du jeu de données ;
- `GET /unique-values` : valeurs uniques d'une colonne ;
- `GET /groupby` : regroupement et agrégation ;
- `GET /filter-by` : filtrage par catégorie ;
- `GET /quantile` : sélection selon un quantile.

## Exemples

Afficher les deux premières lignes :

```text
https://portfolio.vatinel.fr/fastapi-test/preview?n=2
```

Calculer le revenu mensuel moyen par département :

```text
https://portfolio.vatinel.fr/fastapi-test/groupby?column=Department&target=MonthlyIncome&aggregator=mean
```

Filtrer les employés du département `Sales` :

```text
https://portfolio.vatinel.fr/fastapi-test/filter-by?column=Department&cat=Sales
```

## Technologies

- Python
- FastAPI
- Uvicorn
- Pandas
- OpenPyXL
- Caddy


## Limites

Cette API est un projet pédagogique :

- elle ne possède pas de système d'authentification ;
- les paramètres transmis par l'utilisateur ne sont pas tous validés ;
- certaines requêtes incorrectes peuvent produire une erreur HTTP 500 ;
- elle n'est pas prévue pour traiter des données personnelles, confidentielles ou sensibles.
