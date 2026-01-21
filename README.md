# Gender Me

## Introduction

GenderMe est un projet de Data Science que je mêne dans le but de montrer mes capacités dans le domaine informatique et de la science des données. GenderMe se veut être un petit site internet utilisable pour identifier le genre d'une personne basé sur son prénom uniquement. 

## Contexte

Dans le cadre de mon Master en Science de l'Information, j'ai effectué mon projet de recherche principale sur les solutions commerciales disponibles pour inférer le genre d'une personne sur la base de son nom et prénom. Le but à été de produire un classement de ces solutions et services ainsi qu'enquêter sur les biais potentiellement présent dans cette industrie. Dans la cadre de ce projet, j'ai eu l'occasion de créer plusieurs jeux de données liant nom et genre que j'ai eu envie d'explorer plus loin. 

## Méthodologie

Cette section parle de l'implémentation technique de GenderMe.

### Machine Learning

#### Data 

##### Origine

Les données utilisés pour entrainer le modèle prédictif proviennent de mon travail de recherche effectué dans le cadre de mon Master. Pour construire le jeu de données complet utilisé, j'ai mixé deux sources : 
- Paris 2024 Olympic Summer Games, disponible sur Kaggle a l'addresse [suivante](https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games)
- Wikidata

Dans le cas de Kaggle, le jeu de données était déjà dans une forme relativement bien organiser avec peu de preprocessing nécessaires.

Dans le cas de Wikidata, j'ai utilisé [QLever](https://qlever.cs.uni-freiburg.de/wikidata) pour faire une recherche SPARQL afin de relever un total de 5000 personnes provenant de continent different avec une parité équivalente de genre. 

Après avoir enlevé les dupliqués dans les deux cas, j'ai également fait le choix d'enlever les noms composés (deuxième prénom) afin de permettre un séparation automatique des noms et des prénoms au lieu de faire cela manuellement. Ceci est l'un des points de critiques du projet. 

Un fois concatener, le jeu de données contient 13019 prénoms. 

##### Features

Les modèles ML ne peuvent pas traiter une string comme un prénom directement. Pour pouvoir continuer le projet, j'ai utilisé des techniques de NLP afin de vectorizer mes données dans une forme utilisable pour un modèle supervisé. J'ai choisi de relever les type de caractéristiques suivantes : 
- Des n-grams sur la structure du prénoms
- La dernière lettre d'un prénom

La dernière lettre d'un prénom est souvent fortement prédictive du genre de la personne. Par example, les prénom finissant en "a" sont plus souvent féminin (90% dans mon jeu de donnée) tandis que les noms finissant en "o" sont plus souvent masculin (85%).

Utilisé des n-grams est la technique la plus approchable pour vectorizer des strings courte commes des prénoms. J'ai choisi un range de n-grams de 1 a 2 pour éviter de faire exploser la dimensionalité de mon jeu de données, mais quand même avoir une bonne exploration de l'espace de mes données. 


#### Modèle

##### Selection

LOL I DIDN't DO ANY SELECTION I WENT ON GEEKSFORGEEKS, LOOKED UP CLASSIFICATION MODEL AND TOOK THE ONE THAT THEY WERE SAYING HAD THE BEST PERF

##### Selection des hyperparametres

Afin de choisir les hyperparametres optimaux, j'utilise Optuna, une librairie dédicacé a ce but qui propose une méthode de recherche plus efficace que GridSearchCV de sci-kit learn. 


## Analyse métier

### Use case du projet

Ce type de projet pourrait être utilisé afin de bénéficier de plus d'informations sur des clients dont seul le nom est connu. Ceci a des applications en marketing lorsque certaines démographiques sont plus sensibles à differents type de publicité. En ciblant plus précisement les démographiques, l'éfficacité du marketing est augmenté. Je tiens a préciser qu'il est débattable qu'utiliser le nom est la méthode la plus efficace pour définir le genre. 

Le projet peut aussi avoir une utilité dans un cadre de recherche, notamment dans les sciences sociales. Faire des recherches sur l'effet du genre dans differents contexte est parfois compliqué par le fait que le genre des personnes n'est pas disponible. Ce projet permettrait alors de n'avoir besoin que du nom pour obtenir des données genrés. A noter que sa précision ne permet 








