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

## Etape 4 : Jouer

- Lancement

Objectif :

> Allez tout en haut du donjon.
>
> Vous allez utiliser différentes commandes linux afin de vous déplacer dans le jeu

🚩 Vous devez faire un plan afin de vous retrouver dans ce jeu !

  * Appuyer sur Entrée pour continuer
  * Faire Ctrl+C
  * Puis entrer 

- Mission 1 :

  Taper la commande ci'dessous pour découvrir votre première mission :
    
      gsh goal

Faire la mission

Taper la commande : gsh check  pour valider votre première mission

    gsh check

> [!NOTE]
> Gameshell a été mis au point par **Pierre Hyvernat** et **Rodolphe Lepigre**.
> https://github.com/phyver/GameShell/blob/master/README-fr.md
