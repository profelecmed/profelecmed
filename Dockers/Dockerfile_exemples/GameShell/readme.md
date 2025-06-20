# GameShell

Nous allons faire le jeu Gameshell pour apprendre les commandes Linux.


## Etape 1 
* Créer un dossier sur le bureau
* Nommer le dossier sans espace,     Exemple **gamshellciel**
* Copier le fichier
  * dockerfile
 

## Etape 2
sous windows:
* Lancer Docker Descktop

## Etape 3
* Ouvrir le powershell , MAJ + Clic
- A partir de Dockerfile on crée une image docker.

         docker build -t gameshellciel .
  
- Créer et démarre un conteneur à partir d’une image.

         docker run -it gameshellciel

- Attendre
  * Il démarre dnas le terminal

- Lancement
  * Appuyer sur Entrée pour continuer
  * Faire Ctrl+C
  * Puis entrer 

- Mission 1 :

  Taper la commande ci'dessous pour découvrir votre première mission :
    
      gsh goal

> [!NOTE]
> Gameshell a été mis au point par **Pierre Hyvernat** et **Rodolphe Lepigre**.
> https://github.com/phyver/GameShell/blob/master/README-fr.md
