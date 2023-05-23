#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include  "generer-carte.h"


//Chaque noeud peut avoir deux fils
struct arbre {
    sCarte* carte;
    struct arbre* FD;
    struct arbre* FG;
};
typedef struct arbre sArbre;

void placer_carte_arbres(sCarte tableau_carte[], sArbre* arbre1, sArbre* arbre2, sArbre* arbre3);
sArbre* placer_carte_un_arbre(sArbre* racine, sCarte tableau_carte[], int num_arbre);

