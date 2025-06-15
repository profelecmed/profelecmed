# Nmap Scanne adresse IP du réseau

nmap               |  Permet d'analyser les ports et de faire un mapping, Exemple : nmap -p 80 192.168.1.40 ici on scanne le port 80 de l'adresse ip , 80/tcp closed http

Support:

* VM1 : Kalolinux-
* VM2 : Metsploitable

Le réseau :
* Nous allons utiliser dans notre exemple Réseau privée hôte

### Objectif
✨ Ici on va scanner le réseau pour trouver l'adresse Ip de la VM2.

### Détrminer votre adresse IP:

    ip a

Exemple on va obtenir 192.168.2.10

### Scanner le réseau à la recherche de l'IP de la machine 2

Sous Kalilinux lancer Nmap
* ici l'adresse IP du réseau est 192.168.2.0
* Son masque est 255.255.255.0  ou /24

        nmap -v -sb 192.168.2.0/24

* -V printe version number
  
 
On obtient: 

> ✖️ Nmap scan report for 192.100.2.2 [host down]
>
> ✖️  Nmap scan report for 192.100.2.2 [host down]
>
> ✖️ ...
>
>
>✔️ Nmap scan report for 192.100.2.XX **host is up**
>

Nous avons donc trouver notre deuxième machine, VM Metsploitable.  **192.100.2.XX**
