# Jay-Z-Entertainment-Movie-Recommendation
Jay-Z Entertainment Movie Recommendation: Integration of Big Data and AI


# Recommandation de Films Jay-Z Entertainment

**Rapport**

*Par : Yassine Harrati*

*Samedi 09 Decembre 2023*

## Introduction
Jay-Z Entertainment entreprend un projet novateur visant à révolutionner l'expérience de recommandation de films en intégrant le Big Data et l'intelligence artificielle. Cette initiative vise à améliorer les suggestions de films en temps réel en utilisant les données de MovieLens. Le projet s'appuie sur des technologies de pointe telles qu'Apache Spark, Elasticsearch, Kibana, et Flask pour créer un système de recommandation de films personnalisé et dynamique.

## Planification
![gantt](https://github.com/yaserrati/Jay-Z-Entertainment-Movie-Recommendation/assets/88887542/9b7e59dc-633c-43bc-94d3-323149caca7b)


## Flux de projet
<img width="626" alt="Cmovies project flow" src="https://github.com/yaserrati/Jay-Z-Entertainment-Movie-Recommendation/assets/88887542/255353fe-8129-4982-865c-0a7a2e1c65a3">


## Besoin du Projet

## Cadre Technique

### Flask
Utilisé pour créer des points de terminaison afin de récupérer les données de la source. Facilite la communication avec le modèle de recommandation pour garantir des réponses rapides et précises.

### Kafka
Employé pour établir une connexion efficace entre la source de données et la destination dans le pipeline de streaming. Permet une mise à l'échelle aisée du pipeline, garantissant la gestion fluide des flux de données.

### Spark (Pyspark)
Pyspark a été utilisé pour la transformation des données provenant de la plateforme JAY-Z en temps réel. SparkMllib a été exploité pour l'entraînement et le déploiement du modèle de recommandation, offrant une approche puissante pour le traitement des données massives.

### Elasticsearch (Elastic Cloud)
Fonctionne comme une base de données centralisée pour stocker les données nécessaires à l'analyse et à la recommandation de films. Agit en tant que moteur de recherche, offrant des fonctionnalités avancées pour des requêtes complexes et rapides.

### Kibana
Utilisé pour établir une communication efficace avec Elasticsearch. Facilite la création de visualisations personnalisées et permet des analyses en temps réel, renforçant ainsi la compréhension des données et des performances du système.

## Producer

**1. Importation de Bibliothèques :**
Le script utilise différentes bibliothèques, dont `requests` pour la communication avec l'API, `confluent_kafka` pour l'intégration avec Kafka, `time` pour introduire des délais, et `json` pour la sérialisation des données.

**2. Configuration du Producteur Kafka :**
Le producteur Kafka est configuré avec les paramètres nécessaires, tels que l'adresse des serveurs d'amorçage et un identifiant de client.

**3. Définition de l'URL de l'API :**
L'URL de l'API est définie pour pointer vers le point de terminaison Flask qui fournit des informations sur les films. Elle inclut un espace réservé pour le numéro de page afin de permettre la récupération de données paginées.

**4. Fonction de Récupération et de Production :**
La fonction principale, `fetch_data_and_produce`, gère la récupération de données depuis l'API en fonction du numéro de page fourni. Elle sérialise ensuite les données et les envoie à la topic Kafka 'movies'.

**5. Boucle Principale de Récupération de Données :**
Le script utilise une boucle pour récupérer et produire continuellement des données depuis l'API de manière paginée jusqu'à ce qu'aucune donnée supplémentaire ne soit disponible.

## Consumer

**1. Importation de Bibliothèques :**
Le script importe les bibliothèques nécessaires, telles que `Elasticsearch` pour l'intégration avec Elasticsearch, `confluent_kafka` pour la consommation de Kafka, `json` pour la désérialisation des données, `datetime` pour la gestion des horodatages, et `PySpark` pour des capacités supplémentaires de traitement des données.

**2. Configuration du Consommateur Kafka :**
Le consommateur Kafka est configuré avec l'adresse du courtier, un identifiant de groupe de consommateurs et des paramètres pour la gestion des décalages.

**3. Configuration d'Elasticsearch :**
Une connexion à Elasticsearch est établie, en spécifiant les informations d'hôte et de port.

**4. Fonction de Traitement des Données :**
La fonction `clean_data` est responsable du traitement des données reçues. Cela inclut la manipulation des horodatages, la conversion des types de données et la création d'un champ de date formaté.

**5. Mapping d'Index Elasticsearch :**
Le script définit le mapping pour l'index Elasticsearch, spécifiant les types de données et les formats pour les champs indexés.

**6. Création de l'Index :**
L'index Elasticsearch est créé avec le mapping spécifié pour préparer l'insertion de données.

**7. Boucle Principale de Traitement des Messages Kafka :**
Le script poll continuellement les messages de la topic 'movies' de Kafka, décode le message, traite les données en utilisant la fonction `clean_data`, et indexe les données nettoyées dans Elasticsearch.

## Analyse avec Elasticsearch et Kibana

### Indexation dans Elasticsearch
Les données sont stockées dans un index Elasticsearch nommé `index_movies` pour faciliter l'analyse avec Kibana.

### Tableau de bord Kibana
Un tableau de bord Kibana complet a été conçu pour une analyse approfondie. Il intègre différentes visualisations telles que des graphiques à barres et des diagrammes pour fournir une vue d'ensemble complète des données stockées.

## API de Recommandation de Films
![image](https://github.com/yaserrati/Jay-Z-Entertainment-Movie-Recommendation/assets/88887542/9d30182e-746e-45b6-b8fd-c67572b4192f)


### Modèle d'Apprentissage Automatique - ALS
L'API de recommandation utilise le modèle d'apprentissage automatique Alternating Least Squares (ALS) à la fois pour l'entraînement et pour fournir des recommandations de films aux utilisateurs. ALS s'est révélé efficace pour générer des suggestions de films personnalisées basées sur les préférences des utilisateurs.

## Confidentialité et Gouvernance des Données

### Conformité au RGPD
En stricte conformité avec le Règlement Général sur la Protection des Données (RGPD), les données personnelles et sensibles sont méticuleusement supprimées et évitées dès le départ.

### Stratégie de Gouvernance des Données
L'objectif global de notre stratégie de gouvernance des données est de garantir la conformité au RGPD, de protéger contre les accès non autorisés et d'établir un cadre de surveillance continue. Cette stratégie englobe l'alignement réglementaire, la minimisation de l'utilisation des données personnelles, la suppression régulière des données sensibles, des mécanismes de surveillance continue, la transparence dans le traitement des données, la garantie de la qualité et de l'intégrité des données, une documentation détaillée, et un engagement envers l'amélioration continue.

Pour mettre en œuvre cette stratégie, des politiques claires ont été développées, des sessions de formation organisées, des procédures de suppression des données mises en place, des contrôles d'accès définis, des protocoles de surveillance établis, des canaux de communication instaurés, et des mesures d'assurance qualité des données implémentées.

## Conclusion

En conclusion, ce projet intègre de manière transparente le Big Data, l'apprentissage automatique et des technologies de pointe, marquant une étape significative pour Jay-Z Entertainment. En exploitant stratégiquement les données utilisateur, les informations sur les films et le streaming en temps réel avec Kafka et Spark, nous avons réussi à créer un système innovant de recommandation de films personnalisé. Conforme aux normes de protection des données, cette solution promet une expérience utilisateur optimale et des suggestions cinématographiques pertinentes. En résumé, notre projet ouvre de nouvelles perspectives d'innovation et renforce la compétitivité de Jay-Z Entertainment dans le domaine du divertissement.
