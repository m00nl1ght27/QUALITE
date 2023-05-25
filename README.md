# Projet NCat  	
![.](https://github.com/m00nl1ght27/QUALITE/blob/main/cat-nyan-cat.gif)
## cdp : Romain Desriac

Site internet pour récupérer des information d'utilisateur, ces informations sont stockées sur une BDD.

## Table des matières

- [Installation](#installation)
- [Logiciels utilisés](#Logiciels)
- [Plugin Jenkins](#Plugins)
- [Utilisation](#utilisation)
- [Infrastructure](#Infrastructure)
- [Syntaxe](#syntaxe)
- [Personnes présente sur le projet](#Personnes)
- [Tâches à réalisées](#A_faire)
- [Tâches finalisées](#Fini)

## Installation

[Instructions d'installation du projet. Inclure les prérequis, les étapes d'installation et les dépendances nécessaires.]

installation de docker docker : 

`sudo apt update `  
`sudo apt upgrade `  

`sudo apt install docker.io `  
`sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`  
`sudo chmod +x /usr/local/bin/docker-compose`  

`sudo systemctl start docker`  
`sudo systemctl enable docker`  


Installation de Jenkins et sonarQube sur docker : 

`sudo docker pull sonarqube`  
`sudo docker pull jenkins/jenkins`  


`sudo docker start sonarqube`  
`sudo docker start jenkins`  


`sudo docker restart sonarqube`  
`sudo docker restart jenkins`  

[Liaison entre SonarQube et Jenkins](https://github.com/m00nl1ght27/QUALITE/tree/main/Liaison%20SonarQube%20%26%20Jenkins)

[Configuration du build Jenkins](https://github.com/m00nl1ght27/QUALITE/tree/main/Config%20Build%20Jenkins)

![.](https://github.com/m00nl1ght27/QUALITE/blob/main/chaima.png)

## Logiciels

* Visual Studio Code 1.78
* MariaDB Serveur 11.2

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

Machine 	utilisation
Debian 11 	heberge les conteneurs docker
conteneur SonarQube 	verification du github, heberge les versions du site
conteneur Jenkins 	verification du github, heberge les version du site
NGinx 	deploiment du site
conteneur MariaDB 	stokage des données

![.](https://github.com/m00nl1ght27/QUALITE/blob/main/image.png?raw=true)

### Spec

* Systeme d'exploitation : Debian 11
* Architecture : x64
* Nombre de processeur : 2
* RAM : 8Gio
* Type de stockage : SSD premium LRS
* Espace de stockage : 30Go

## Syntaxe

Nom des variables : sans maj avec des underscores pour espace   
Nom des fonctions : Avec maj avec des underscores pour espace et un comentaire explicatif au dessus 

## Personnes

| Personne       | Rôle                             |
|----------------|----------------------------------|
| Romain Desriac | Chef de projet                   |
| Camille Herve  | Responsable Jenkins              |
| Kleden Bizien  | responsable SonarQube            |
| Gaël Bouillies | Responsable front-end / back-end |
| Hugo Faigner   | Respinsable GitHub               |

## A faire

| Tâches                         | Description                                                        | DeadLine   | Criticité |
|--------------------------------|--------------------------------------------------------------------|------------|-----------|
| Améliorer l'animation du NCat  | Ajouter un NCat en plus poour une double rotation                  | 26/05/2023 |     1     |
| Intérger la fonction de scroll | Ajout de la possibilité de scroll quand on est zoomer              | 25/05/2023 |     2     |
| Finir la BDD                   | Finaliser le liens entre la bdd et la front-end                    | 25/05/2023 |     4     | 
| Envoie mail build failed       | Configurer l'envoi d'un mail en cas de build non réussi            | 26/05/2023 |     2     |

## Fini

| Tâches                              | Responsable                                    | Derniére modification |
|-------------------------------------|------------------------------------------------|-----------------------|
| Mise en place du github             | Romain DESRIAC                                 | 23/05/2023            |
| Mise en place conteneur             | Camille HERVE                                  | 23/05/2023            |
| Mise en place front-end / back-end  | Gaël BOUILLIES 	                               | 23/05/2023            |
| Mise en place SonarQube 	          | Romain DESRIAC                                 | 23/05/2023            |
| Initialisation github 	            | Romain DESRIAC 	                               | 23/05/2023            |
| Mise en place infrastructure Azure  | Kleden BIZIEN                                  | 23/05/2023            |
| Mise en place bdd 	                | Gaël BOUILLIES                                 |	24/05/2023           |
| Creation ReadMe 	                  | Hugo FAIGNER                                   |	24/05/2023           |
| Mise en place Jenkins               |	Kleden BIZIEN & Camille HERVE                  |	24/05/2023           |
| Installation des plugins Jenkins    | Romain DESRIAC & Camille HERVE & Kleden BIZIEN |	23/05/2023           |
| Connexion entre Jenkins & SonarQube | Kleden BIZIEN & Camille HERVE                  | 24/05/2023            |

## Version 1.02

Ajout de la fonction dark mode

## Version 1.01

Ajout du NCat

## Version 1.0

Sorti du site dans sa version la plus basic
