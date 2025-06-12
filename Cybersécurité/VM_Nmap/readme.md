# Nmpa

Support:

* VM1 : Kalolinux-
* VM2 : Metsploitable

Le réseau :
* Nous allons utiliser dans notre exemple Réseau privée hôte

### Détrminer votre adresse IP:

    ip a

Exemple on va obtenir 192.168.2.10

### Scanner le réseau à la recherche de l'IP de la machine 2

    nmap -v -sb 192.168.2.0/24
