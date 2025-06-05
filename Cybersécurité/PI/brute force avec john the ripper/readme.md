# brute force avec john the ripper

Support : Raspberry Pi

### Mise en situation :
Votre société Ciel_Pentester vient de réaliser un audit sur la société XX afin d’identifier la surface d’attaque. Après une cartographie complète, il apparaît des informations sensibles. 

Nous avons détecté une mauvaise gestion de droits :

Exemple : Des répertoires sont accessible par des utilisateurs non identifiés au réseau.  
Le N°1 est nommé Bonnes pratiques.  Piste 1 : Ce répertoire peut-il contenir des données sensibles. 

Le N°2 est nommé …….  Il est encore plus intéressant car il contient un fichier nommé Secret.7z , il est  zippé et protégé par un mot de passe.

Nous avons récupéré toutes ses informations et nous les avons placées dans un fichier zippé Pentesting.7z

### Objectif :
Vous devez découvrir les informations contenues dans le fichier Secret.7z

-----

## Prérequis 1 :

#### Vérifier l'installation de **John the Ripper**

       apt show john

Si cela ne fonctionne pas vous devez voir la partie 1 Prérequis


## Prérequis 2 :

#### Vérifier l'installation de **Seven zip 7zr**

       apt show p7zip


Si cela ne fonctionne pas vous devez voir la partie 1 Prérequis

Créer sur le Desktop un répertoire dirjohn

Télécharger le fichier Secret.7Z

Copier le fichier Secret.7é dans le répertoire dirjohn

Ouvrir un terminal:
se rendre dans le répertoire dirjohn sur le bureau
faire ls et virifier qu'il il a bien le ficher Secret.7z
pour connaître toutes les commandes disponible 

       john
S'il n'y a pas la commande voulue exemple 7z2john

       sudo apt install git build-essential libssl-dev zlib1g-dev libbz2-dev libpcap-dev pkg-config yasm

7z2john Secret.7z > Secret.txt
faire ls et virifier qu'il il a bien le ficher Secret.txt

