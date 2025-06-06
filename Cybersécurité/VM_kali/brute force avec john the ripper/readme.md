# brute force avec john the ripper

Support : VM avec Kalilinux

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

Ouvrir un terminal:

       john

Vous devez obtenir une version avec l'extension jumbo , exemple John the Ripper 1.9.0-jumbo-1 ....

## Méthode


7z2john Secret.7z > Secret.txt
faire ls et virifier qu'il il a bien le ficher Secret.txt


