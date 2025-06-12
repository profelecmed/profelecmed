# Mise en réseau de vos machines virtuelles

Support:  
* VM1 : Kalolinux
* VM2 : Debin

### Réseau initial:

Quand vous créez une machine virtuelle la première fois, VirtualBox active par défaut une carte réseau virtuelle et sélectionne le mode “Network Address Translation” (**NAT**)

VirtualBox fournit jusqu’à huit cartes Ethernet PCI virtuelles pour chaque machine virtuelle.

Ici nous allons utiliser uniquement : 
* ✅ **adapter1**
* ✅ **adapter2**

VirtualBox offre plusieurs modes d'interface résea (NAT , interne, ....

| Réseau       | VM -> Externe | Externe -> VM | VM <-> Hôte | VM <-> VM |
| :---------------- | :----------------------------- | :---------------------------- | :------------------------ | :---------------------------------- |
| **NAT** | Oui                            | Non    | Hôte -> VM  | Non                      |
| **Accès par pont** | Oui                            | Oui                           | Oui                       | Oui                                 |
| **Réseau interne** | Non                            | Non                           | Non                       | Oui                                 |
| **Privé hôte** | Non                            | Non                           | Oui                       | Oui                                 |
| **Réseau NAT** | Oui                            | Non    | Oui                       | Oui                                 |


Nous allons utiliser dans notre exemple **Réseau privée hôte**
* 🚩 ici Pas d'accès à Internet pour les VMs.
* Il y a communication entre VM.
* Il y a communication interne avec l'hôte et le localhost.

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
