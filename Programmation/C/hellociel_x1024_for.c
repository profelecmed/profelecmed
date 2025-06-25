/* Hellociel x 1024  

Le C en ligne : https://www.mycompiler.io/fr/new/c */

#include <stdio.h> // Nécessaire pour printf

int main() {
    for (int i = 1; i <= 1024; i++) {
        printf("%d: Hello Ciel !\n", i); // Correct : %d est un "placeholder" pour un entier, et 'i' est l'argument correspondant.
    }
    return 0; // Indique que l'exécution s'est déroulée avec succès
}
