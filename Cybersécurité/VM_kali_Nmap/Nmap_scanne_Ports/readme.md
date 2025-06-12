# Nmap Scanne des Ports ouverts sur une machine

nmap               |  Permet d'analyser les ports et de faire un mapping, Exemple : nmap -p 80 192.168.1.40 ici on scanne le port 80 de l'adresse ip , 80/tcp closed http

Support:

* VM1 : Kalolinux-
* VM2 : Metsploitable

Le réseau :
* Nous allons utiliser dans notre exemple Réseau privée hôte


Ici on va scanner pour trouver les ports ouverts de la VM2.

### Pré-requis

* Connaitre l'adrese IP de la cible ici la VM2. voir https://github.com/profelecmed/profelecmed/blob/main/Cybers%C3%A9curit%C3%A9/VM_kali_Nmap/Nmap_scanne_IP/readme.md

### Trouver les ports ouverts

    nmap 192.168.2.XX

réponse attendue:
>
> Starting Nmap 7.95 (https://nmap.org) at ....
>
> ....
>
> ....
>
> 21/tcp   open  ftp
>
> **XX**/tcp   open  ssh
>
> 80/tcp    open http
>

Nous avons donc trouver les ports ouverts pour notre deuxième machine, VM Metsploitable.  Le port XX pour le ssh.
