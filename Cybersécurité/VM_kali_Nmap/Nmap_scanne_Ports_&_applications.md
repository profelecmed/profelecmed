# Nmap Scanne des Ports ouverts et applications sur une machine

nmap               |  Permet d'analyser les ports et de faire un mapping, Exemple : nmap -p 80 192.168.1.40 ici on scanne le port 80 de l'adresse ip , 80/tcp closed http

Support:

* VM1 : Kalolinux-
* VM2 : Metsploitable

Le réseau :
* Nous allons utiliser dans notre exemple Réseau privée hôte

### Objectif:

✨ Ici on va scanner pour trouver les ports ouverts de la VM2.

### Pré-requis

* Connaitre l'adrese IP de la cible ici la VM2. voir https://github.com/profelecmed/profelecmed/blob/main/Cybers%C3%A9curit%C3%A9/VM_kali_Nmap/Nmap_scanne_IP/readme.md

### Trouver les ports ouverts et applications

Sous Kalilinux lancer Nmap

    nmap -sV 192.168.2.XX

-sV va nous permettre d'obenir des informations sur les versions des services et applications

réponse attendue:
>
> Starting Nmap 7.95 (https://nmap.org) at ....
>
> ....
>
> ....
>
>Port     STATE    Service    Version
>
>21/tcp   open  ftp   vsf......
>
> **XX**/tcp   open  ssh   .....
>
> 80/tcp    open http  !apache httpd 2.2.8  ..... 
>
Nous avons donc trouver les ports ouverts, les services et les informations sur les version installées pour notre deuxième machine, VM Metsploitable.  Le port **XX pour le ssh**.

