# SSH

Support:

* VM1 : Kalolinux
* VM2 : Debin 12

Réseau :

Le réseau doit être en **Accès par pont**
https://github.com/profelecmed/profelecmed/blob/main/Cybers%C3%A9curit%C3%A9/VM_Mise%20_en_r%C3%A9seau_.md

## Objectif:
✨ Se connecter à partir de la machine kalilinux sur la machine Debian 12. On va utiliser le protocole ssh **Secure Shell**

-----

## Vérification si ssh sur la machine Debian 12

    systemctl status ssh

* Exemple de non présence : unit ssh could not be found

Vérification si la commande est disponible:

    which ssh

* Si elle retourne le chemin alors elle est déjà installé.  /usr/bin/ssh



### Installer openssh-server sur la machine Debian 12

mise à jour des dépot

    apt update

installatopn openssh-serveur
    
    apt install openssh-server

## Vérification si ssh sur la machine Debian 12

    systemctl status ssh

* Exemple DE présence :
* 
> ssh.service - OpenBSD SECURE SHELL SERVER
> 
> Loaded : ...........
> 
> Active : Active ....
> 
> ....
> 

## Utilisateur sur la machine Debian 12

    whoami

Exemple : idpatron


-----

## Lancer la connexion ssh à partir de la VM Kalilinux 

ouvrit un terminal

    su

mdp

    ssh idpatron@192.168.56.XX

Exemple vous êtes connecté  ✔️  id@debian:


-----

## Arrêter la connexion ssh à partir de la VM Kalilinux 

    exit

Connection to 192.168.56.XX closed
