#define _CRT_SECURE_NO_WARNINGS

#include  "generer-carte.h"


// Fonction pour mélanger les cartes
// @param : Tableau des 52 cartes créées dans l'ordre

void melange(sCarte tableau_cartes[], sCarte tableau_cartes_rand[]) {

  int max = 52, nb_random;
  
  sCarte carte_temp;

  //Initialisation du nb random
  srand(time(NULL));

  for (int i = 0; i < 52; i++)
  {
    //nb random générer entre 0 et 51 et décrémenté au fur et à mesure
    nb_random = rand() % max;

    //On place la carte tirer au hasard dans le tableau de cartes non triées
    tableau_cartes_rand[i] = tableau_cartes[nb_random];

    //On place la dernière carte du tableau dans une carte temporaire
    carte_temp = tableau_cartes[max-1];

    //Puis on place la carte tirée au hasard à la fin du tableau pour ne pas la tirer deux fois
    tableau_cartes[max-1] = tableau_cartes[nb_random];

    //On échange de place entre la dernière carte et la carte tirée
    tableau_cartes[nb_random] = carte_temp;

    //Décrémentation du nombre max pour que le nombre random soit
    max --;
  }
  
}


// Fonction pour générer les 52 cartes cartes

void generer(sCarte tableau_cartes_rand[]) {

    sCarte carte;
    sCarte tableau_cartes[52];
    char tab_couleur[4] = { 'C','T','P','K' }; // C = carreau, T = trefle, K = coeur, P = pique
    int compt_tab = 0;

    //Boucle sur les couleurs
    for (int i = 0; i < 4; i++)
    {
        //Boucle sur les numéros (de l'as : 1 au roi : 13)
        for (int y = 1; y < 14; y++)
        {
            carte.couleur = tab_couleur[i];
            carte.numero = y;
            carte.visible = 0;
            carte.numArbre[0] = 0;
            carte.numArbre[1] = 0;
            tableau_cartes[compt_tab] = carte;
            compt_tab++;
        }
    }

    melange(tableau_cartes, tableau_cartes_rand);
}