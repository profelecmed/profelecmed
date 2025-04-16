# Dockerfile

Un Dockerfile est un fichier texte écrit avec un des régles.
C'est donc un fichier texte contenant des instructionx afin de construire une image Docker.

## Etape 1 
* Créer un dossier sur le bureau
* Nommer le dossier sans espace,     Exemple **mon_dossier_perso_dockerfile**
* Copier votre fichier dockerfile

## Etape 2
sous windows:
* Lancer Docker Descktop

## Etape 3
* Ouvrir le powershell , MAJ + Clic
- A partir de Dockerfile on crée une image docker.

         docker build -t monimage .
  
- Créer et démarre un conteneur à partir d’une image.

         docker run monimage
