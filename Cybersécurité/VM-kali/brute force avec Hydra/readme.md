# Brute force avec Hydra

🚩 Attention il est interdit d'accéder à des systèmes sans autorisation🏴‍☠️

Support : 

* VM Kalilinux avec utilisation de **Hydra**
* VM Debian 12

Réseau :

Le réseau doit être en **Accès par pont**
https://github.com/profelecmed/profelecmed/blob/main/Cybers%C3%A9curit%C3%A9/VM_Mise%20_en_r%C3%A9seau_.md

### Mise en situation :
>  Votre société Ciel_Pentester vient de réaliser un audit sur la société XX afin d’identifier la surface d’attaque.
>
> Après une cartographie complète, vous avez découvert une machine debian.
>
> Nous allons utiliser Hydra. Hydra est un outil de test de pénétration utilisé pour effectuer des attaques par force brute sur divers services, y compris SSH.

### Objectif :

✨ Vous devez arriver à vous connecter en SSH à la machine Debian à partir de Kalilinux. Vous devez découvrir le mot de passe de la session user.

-----
Une **attaque par brute force** teste un grand nombre de combinaisons pour trouver le bon mot de passe.
Ici nous allons utiliser une variante de l'attaque brute force, **attaque par dictionnaire**


## Prérequis 1 :

Nous allons utiliser un dictionnaire

* rockyou

Vérifier la présence de rockyou dans le répertoire **worklists**. Le chemin est /usr/share/wordlists


-----

## Méthode

Lancer Hydra sous Kalilinux

    hydra -l idpatron -p /usr/share/wordlists/rockyou.txt -u -e s ssh://192.168.56.XX

Détails de la commande
>
> -l Ici un identifiant unique à tester
>
> -p /../../.. Nous donne le chemin du répertoire qui contient le dictionnaire.
>
>Ici le dictionnaire est rockyou.txt
>
>-u Force Hydra à tester chaque mot de passe un par un sans parallélisation excessive, ce qui peut éviter de surcharger le serveur cible.
>
>-e s Indique à Hydra d’essayer également le mot de passe correspondant au nom d’utilisateur
>
> ssh://192.168.56.XX L’attaque cible le service SSH de la machine Debian située à l’adresse IP /192.168.56.XX


Réponse :
>
> hydra ....
>
>...
>
>[22][ssh] host: 192.168.56.XX  login: ippatron  password: mdpdepatron
>

Nous avons bien trouvé notre mot de passe : **mdpdepatron** qui est lié à l'utilisateur **idpatron**

On va faire un test de connection

      ssh idpatron@192.168.56.XX
  
mot de passe : **mdpdepatron**

Exemple vous êtes connecté  ✔️  id@debian:

-----

## Arrêter la connexion ssh à partir de la VM Kalilinux 

    exit

Connection to 192.168.56.XX closed

-----

> [!NOTE]
> Si le mot de passe n'est pas découvert vous pouver utiliser d'autres dictionnaires, allez voir Liste_dictionnaire.md
> https://github.com/profelecmed/profelecmed/blob/main/Cybers%C3%A9curit%C3%A9/VM_kali/brute%20force%20avec%20john%20the%20ripper/Liste_dictionnaire.md


>[!TIP]
>
> Il est important d'avoir un mot de passe robuste.
>
> Voir la CNIL : https://www.cnil.fr/fr/mots-de-passe-une-nouvelle-recommandation-pour-maitriser-sa-securite


