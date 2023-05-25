# Projet NCat  	
![.](https://github.com/m00nl1ght27/QUALITE/blob/main/cat-nyan-cat.gif)
## cdp : Romain Desriac

Site internet pour récupérer des information d'utilisateur, ces informations sont stockées sur une BDD. Avec correction du code par SonarQube & Jenkins

## Table des matières

- [Spec de la machine](#Spec)
- [Installation](#installation)
- [Logiciels utilisés](#Logiciels)
- [Plugin Jenkins](#Plugins)
- [Utilisation](#utilisation)
- [infrastructure](#Infrastructure)
- [Syntaxe](#syntaxe)
- [Personnes présente sur le projet](#Personnes)
- [Tâches à réalisées](#A_faire)
- [Tâches finalisées](#Fini)

## Installation

[Instructions d'installation du projet. Inclure les prérequis, les étapes d'installation et les dépendances nécessaires.]

## Logiciels

* Visual Studio Code 1.78
* MariaDB Serveur 11.2
* NGinx 1.18

* SonarQube 10.0
* Jenkins 2.405

## Plugins

* SonarQube Scanner for Jenkins Version 2.15 
* Parameterized Scheduler Version 1.2
* OWASP Markup Formatter version 159.v25b_c67cs35fb

## Utilisation

Une fois sur le site en local, rentrer les informations dans les champs correspondants.
Quand vous cliquerez sur "enregistrer", cela envoie 

## Infrastructure

| Machine                         | utilisation   |
|--------------------------------|------------|
| Debian 11   | heberge les conteneurs docker |
| conteneur SonarQube | verification du github, heberge les versions du site |
| conteneur Jenkins                   | verification du github, heberge les version du site |
| NGinx| deploiment du site | 
| conteneur MariaDB | stokage des données | 

![.](https://github.com/m00nl1ght27/QUALITE/blob/main/image.png)

## Syntaxe

Nom des variable :
Nom des fonction :

## Personnes

| Personne       | Rôle                             |
|----------------|----------------------------------|
| Romain Desriac | Chef de projet                   |
| Camille Herve  | Responsable Jenkins              |
| Kleden Bizien  | responsable SonarQube            |
| Gaël Bouillies | Responsable front-end / back-end |
| Hugo Faigner   | Respinsable GitHub               |

## A_faire

| Tâches                         | DeadLine   | description | criticité |
|--------------------------------|------------|-------------|-----------|
| améliorer l'animation du NCat  | 26/05/2023 | Ajouter un NCat en plus poour une double rotation | 4 |
| intérger la fonction de scroll | 25/05/2023 | Ajout de la possibilité de scroll quand on est zoomer| 2 |
| Finir la BDD                   | 25/05/2023 | Finaliser le liens entre la bdd et la front-end | 4|
| Fin du projet                   | 26/05/2023 | Finir toute les autre étapes | 4 |
| envoie mail automatique         | 26/05/2023 | Parametrer l'envoie de mail automatioque en cas de build failed en ouvrant le port 25 |1|


## Fini

| Tâches         | Responsable   | Derniére modification |
|----------------|---------------|-----------------------|
| Mise en place du github       | Romain Desriac    | 23/05/2023            |
| Mise en place conteneur        | Camille Herve   |  23/05/2023            |
| Mise en place font-end / back-end        | Gaël Bouillies    | 23/05/2023           |
| Mise en place du SonarQube      | Romain Desriac    | 23/05/2023            |
| Initialisation github        | Hugo Faigner   |  23/05/2023            |
| Mise en place infrastructure Azure      | Kleden Bizien    |  23/05/2023           |
| Mise en place bdd       | Gaël Bouillies    | 24/05/2023           |
| Initialisation ReadMe       | Hugo Faigner   |  24/05/2023            |
| Mise en place Jenkin        | Kleden Bizien &  Camille Herve  |  24/05/2023           |
| Initialisation plugin Jenkin        | Romain Desriac    | 23/05/2023            |

## Version 1.02

Ajout de la fonction dark mode

## Version 1.01

Ajout du NCat

## Version 1.0

Sorti du site dans sa version la plus basic
