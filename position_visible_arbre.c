#define _CRT_SECURE_NO_WARNINGS
#include "position_visible_arbre.h"



sArbre* placer_carte_un_arbre(sArbre* racine, sCarte tableau_carte[], int num_arbre) {

	sArbre* arbre = racine;
	//Initialisation de la mémoire du fils commun
	sArbre* fils_commun = NULL;

	//Racine, soit le noeud 1
	arbre->carte = &tableau_carte[0];
	arbre->FG->carte = &tableau_carte[1];
	arbre->FD->carte = &tableau_carte[2];

	//Initialisation coté gauche
	//Noeud 2
	arbre = arbre->FG;
	arbre->carte = &tableau_carte[1];
	arbre->FG->carte = &tableau_carte[3];
	arbre->FD->carte = &tableau_carte[4];

	//Noeud 4
	arbre = arbre->FG;
	arbre->carte = &tableau_carte[3];
	arbre->FG->carte = &tableau_carte[6];
	arbre->FD->carte = &tableau_carte[7];

	//Noeud 7
	arbre = arbre->FG;
	arbre->carte = &tableau_carte[6];
	arbre->FG->carte = NULL;
	arbre->FD->carte = NULL;

	if (num_arbre == 3) {
		fils_commun = arbre;
	}

	//retour à la racine 
	arbre = racine;

	//Noeud 3
	arbre = arbre->FD;
	arbre->carte = &tableau_carte[2];
	arbre->FG->carte = &tableau_carte[4];
	arbre->FD->carte = &tableau_carte[5];

	//Noeud 5
	arbre = arbre->FG;
	arbre->carte = &tableau_carte[4];
	arbre->FG->carte = &tableau_carte[7];
	arbre->FD->carte = &tableau_carte[8];

	//Noeud 8
	arbre = arbre->FG;
	arbre->carte = &tableau_carte[7];
	arbre->FG->carte = NULL;
	arbre->FD->carte = NULL;

	//retour à la racine 
	arbre = racine;
	arbre = arbre->FD;

	//Noeud 6
	arbre = arbre->FD;
	arbre->carte = &tableau_carte[5];
	arbre->FG->carte = &tableau_carte[8];
	arbre->FD->carte = &tableau_carte[9];

	//Noeud 9
	arbre = arbre->FG;
	arbre->carte = &tableau_carte[8];
	arbre->FG->carte = NULL;
	arbre->FD->carte = NULL;

	//retour à la racine 
	arbre = racine;
	arbre = arbre->FD;
	arbre = arbre->FD;

	//Noeud 10 SOIT LE NOEUD EN COMMUN
	arbre = arbre->FD;
	arbre->carte = &tableau_carte[9];
	arbre->FG->carte = NULL;
	arbre->FD->carte = NULL;

	//Si l'arbre remplis est le premier arbre alors on sauv sont fils tout à droite
	if (num_arbre == 1) {
		fils_commun = arbre;
	}

	return fils_commun;
}

/*
* Fonction pour positionner les cartes dans les arbres
* Toutes les cartes sont cachées
* @param : Tableau de 28 cartes
*/
void placer_carte_arbres(sCarte tableau_carte[], sArbre* arbre1, sArbre* arbre2, sArbre* arbre3) {
	
	//on créé 3 tableau pour chaque arbre 
	sCarte tableau_carte1[10], tableau_carte2[8], tableau_carte3[10];
	sArbre* fils_commun_droite, *fils_commun_gauche;
	
	int compt1 = 0, compt2 = 0;

	for (int i = 0; i < 52; i++) {

		if (i <= 0 && i <= 9) {
			tableau_carte1[i] = tableau_carte[i];
		}
		if (i >= 10 && i <= 17) {
			tableau_carte2[compt1] = tableau_carte[i];
			compt1++;
		}
		if (i >= 18 && i <= 28) {
			tableau_carte3[compt2] = tableau_carte[i];
			compt2++;
		}
	}

	//Dans un premier temps on génère l'arbre de droite et l'arbre de gauche en entier pour récupérer le fils commun
	//génération du premier arbre (à droite)
	fils_commun_droite = placer_carte_un_arbre(arbre1, tableau_carte1, 1);
	//génération du troisième arbre (à gauche)
	fils_commun_gauche = placer_carte_un_arbre(arbre3, tableau_carte1, 3);

	//génération du troisième arbre
	//placer_carte_un_arbre(&arbre1, tableau_carte3, 3);
} 

