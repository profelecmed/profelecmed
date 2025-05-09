# Commandes:

## Configurez le port WAN
                                                            
### Entrer en mode privilégié 
Vous en mode utilisateur Routeur >
**Router >**

    enable
   
  Ou 
  
    en  				                                                               
**Router #**   est le mode commande privilégié.


La validation de cette commande entraîne souvent la demande d’un mot de passe.  Cisco Cisco

Par la suite pour revenir à ce niveau du mode commande, il suffira de taper « CTRL+Z »

-----

### Entrer en config globale 
**Router #**

     configure terminal 
   
  ou   
  
    conf t  				                                                               

**Router(config) #** est le mode de configuration globale.

----

### Entrer en config interface

**Router(config) #**

    interface GigabitEthernet 0/0/0  

- 0/0/0 pour le port combo WAN   ou  0/0/1 pour le port WAN dédié.


**(config-if)#** est le mode config interface 

----

### Configurer une adresse

1️⃣ Cas ou vous êtes en mode DHCP
    
    ip address dhcp

2️⃣  Cas ou vous êtes en static

    ip address  192.168.1.1 255.255.255.0              

Remùplacer l'adresse est le masque par les valeurs donnée par le FAI ou de votre access.

----
### Activer l’interface
    no shutdown

----
###  Quitter le mode de configuration interface 

    exit

----
### Affiche les informations des interfaces

    show ip interface brief

----
### Sauvegarder votre configuration

 Router#

    write memory

  ou

    running-config startup-config
 

