# Mise en réseau de vos machines virtuelles

Support:  
* VM1 : Kalolinux
* VM2 : Debin

### Réseau initial:

Quand vous créez une machine virtuelle la première fois, VirtualBox active par défaut une carte réseau virtuelle et sélectionne le mode “Network Address Translation” (**NAT**)

VirtualBox fournit jusqu’à huit cartes Ethernet PCI virtuelles pour chaque machine virtuelle.

Ici nous allons utiliser uniquement : 
* adapter1
* adapter2

VirtualBox offre plusieurs modes d'interface résea (NAT , interne, ....

Nous allons utiliser dans notre exemple **Réseau privée hôte**, ici Pas d'accès à Internet pour les VMs.

### Réglage pour la VM debian :
* Reseau , mode expert
    * Activer adapter 1
       * Mode d'acces réseau : **Réseau privée hôte**
       * Mode Promiscuité: **Allow All**
       * Câble branché

### Réglage pour la VM kalilinux :
* Reseau , mode expert
    * Activer adapter 2
       * Mode d'acces réseau : **Réseau privée hôte**
       * Mode Promiscuité: **Allow All**
       * Câble branché


### Démarrer les VM:
* VM1 : Kalolinux
* VM2 : Debin

### Rechercher les adressess IP

         ip a
Exemple : 192.168.1.XX pour VM débian
Exemple : 192.168.1.YY pour VM kalilinux


### Vérifier la communication entre machine
* De VM debian a VM kalilinux
  
      ping  192.168.1.YY

* De VM kalilinux à la VM debian
  
      ping  192.168.1.XX
