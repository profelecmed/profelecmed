# GameShell

Nous allons faire le jeu Gameshell pour apprendre les commandes Linux.
Gameshell a été mis au point par **Pierre Hyvernat** et **Rodolphe Lepigre**.

## Etape 1 
* Créer un dossier sur le bureau
* Nommer le dossier sans espace,     Exemple **gamshellciel**
* Copier vos fichiers
  * dockerfile
 

## Etape 2
sous windows:
* Lancer Docker Descktop

## Etape 3
* Ouvrir le powershell , MAJ + Clic
- A partir de Dockerfile on crée une image docker.

         docker build -t gameshellciel .
  
- Créer et démarre un conteneur à partir d’une image.

         docker run -d -p 8080:80 gameciel
