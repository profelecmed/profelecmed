# SSH

Support:

* VM1 : Kalolinux
* VM2 : Debin 12

Réseau :

Le réseau doit être en **Accès par pont**

## Objectif:
✨ Se connecter à partir de la machine kalilinux sur la machine Debian 12.

-----

## Vérification si ssh sur la machine Debian 12

    systemctl status ssh

* Exemple de non présence : unit ssh could not be found

Vérification si la commande est disponible:

    which ssh

* Si elle retourne le chemin alors elle est déjà installé.  /usr/bin/ssh



### installer openssh-server sur la machine Debian 12

mise à jour des dépot

    apt update

installatopn openssh-serveur
    
    apt install openssh-server

## Vérification si ssh sur la machine Debian 12

    systemctl status ssh

* Exemple DE présence :
> ssh.service - OpenBSD SECURE SHELL SERVER
> Loaded : ...........
> Active : Active ....
> ....
> 

-----

## lancer la connexion ssh à partir de la VM Kalilinux 

ouvrit un terminal

    su

mdp

    apt id@192.168.56.XX

