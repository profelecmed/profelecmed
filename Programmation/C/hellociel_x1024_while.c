#include <stdio.h> // Nécessaire pour printf

int main() {
    int i; // Declaring 'i' 
    i = 1; // Initializing 'i' to 1 before the loop

    while (i <= 1024) { // Only the condition goes here, no semicolons needed
        printf("%d: Hello Ciel !\n", i);
        i = i + 1; // Increment 'i' inside the loop
    }

    return 0; // Indique que l'exécution s'est déroulée avec succès
}
