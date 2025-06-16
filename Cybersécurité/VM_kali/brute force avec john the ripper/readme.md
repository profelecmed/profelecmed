# Brute force avec john the ripper

🚩 Attention il est interdit d'accéder à des systèmes sans autorisation🏴‍☠️

Support : 

* Kalilinux (par exemple en VM)
*  john the ripper en mode jumbo

### Mise en situation :
> Votre société Ciel_Pentester vient de réaliser un audit sur la société XX afin d’identifier la surface d’attaque. Après une cartographie complète, il apparaît des informations sensibles.
>
> Nous avons détecté une mauvaise gestion de droits :
>
> Exemple : Des répertoires sont accessible par des utilisateurs non identifiés au réseau.  
>
>Le N°1 est nommé Bonnes pratiques.  Piste 1 : Ce répertoire peut-il contenir des données sensibles. 
>
>Le N°2 est nommé …….  Il est encore plus intéressant car il contient un fichier nommé Secret.7z , il est  zippé et protégé par un mot de passe.

Nous avons récupéré toutes ses informations et nous les avons placées dans un fichier zippé Pentesting.7z

### Objectif :

✨ Vous devez découvrir les informations contenues dans le fichier Secret.7z

-----
Une **attaque par brute force** teste un grand nombre de combinaisons pour trouver le bon mot de passe.
Ici nous allons utiliser une variante de l'attaque brute force, **attaque par dictionnaire**


## Prérequis 1 :
* Sur le bureau créer un répertoire **kalisecret**
* Copier à partir de notre github le fichier **Secret.7Z** ,  🚩 Il faut un mot de passe pour ouvrir ce fichier zippé..
* Copier à partir de notre github le fichier **passwords_top.txt**, c'est notre dictionnaire perso de mot de passe.

## Prérequis 2 :

* Installer 7z si nécessiare
  
Se reporter à 2_Prérequis


## Prérequis 3 :

#### Vérifier l'installation de **John the Ripper**

Ouvrir un terminal:

       john

Vous devez obtenir une version avec l'extension jumbo , exemple John the Ripper 1.9.0-jumbo-1 ....

-----

## Méthode

* Rendez-vous dans le répertoire **kalisecret** sur le bureau avec les commande pwd , ls , cd .. , cd répertoire ,...

* Vérifier qu'il contient le fichier à craker : **Secret.7z**

* #### Extraire le fichier **Secret.zip** avec **7z**

Normalement on vous demande d'**Entrer un mot de passe** , ❌ Vous ne connaissez pas ce mot de passe.

* On va extraire le hash du mot de passe de Secret.7z qui est une archive 7z chiffrée et le rediriger vers un fichier texte.

       7z2john Secret.7z > Secret.txt

* Faire ls et vérifier qu'il il a bien le ficher **Secret.txt**

* on va voir ce que contient le fichier **Secret.txt**

         Cat Secret.txt

On obtient le hash  : Secret.7z:$7z$2$19$0$$16$e56...............................................................

Un hachage est une empreinte numérique d'un mot de passe.

* Utilisation d’un dictionnaire perso afin de gagner du temps sur la recherche du mot de passe. Notre dictionnaire perso est le fichier **passwords_top.txt**

       john --wordlist=passwords_top.txt Secret.txt

  Attendre quelles secondes.... please wait

réponse attendue:
>
> Using default input encoding: UTF-8
>
> Loaded 1 password hash (7z, 7-Zip archive encryption [SHA256 256/256 AVX2 8x AES])
>
> Cost 1 (iteration count) is 524288 for all loaded hashes
>
> Cost 2 (padding size) is 2 for all loaded hashes
>
> Cost 3 (compression type) is 2 for all loaded hashes
>
> Cost 4 (data length) is 14 for all loaded hashes
>
> Will run 4 OpenMP threads
>
> Press 'q' or Ctrl-C to abort, almost any other key for status

**........mdp.......**               (Secret.7z)   


* #### Extraire le fichier **Secret.zip** avec **7z**

Normalement on vous demande d'**Entrer un mot de passe** , ✔️ Vous connaissez maintenant le mot de passe **........mdp.......**   .

VOUS POUVEZ LIRE LE MESSAGE SECRET : ..............................................

> [!NOTE]
> Si le mot de passe n'est pas découvert vous pouver utiliser d'autres dictionnaires, allez voir Liste_dictionnaire.md
> https://github.com/profelecmed/profelecmed/blob/main/Cybers%C3%A9curit%C3%A9/VM_kali/brute%20force%20avec%20john%20the%20ripper/Liste_dictionnaire.md


>[!TIP]
>
> Il est important d'avoir un mot de passe robuste.
>
> Un mot de passe solide et l’authentification à deux facteurs (2FA).
>
> Voir la CNIL : https://www.cnil.fr/fr/mots-de-passe-une-nouvelle-recommandation-pour-maitriser-sa-securite



