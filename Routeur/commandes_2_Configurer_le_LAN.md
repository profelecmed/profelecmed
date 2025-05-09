# Commandes 2:

## Configurer le port LAN
Le routeur C1111-4P a un switch intégré (avec 4 ports LAN)
0/1/0 à 0/1/3 pour les port LAN.
                                                            
### Entrer en mode privilégié 
Vous en mode utilisateur 
**Router >**

    enable
   
  Ou 
  
    en  				                                                               
**Router #**   est le mode commande privilégié.


La validation de cette commande entraîne souvent la demande d’un mot de passe.  Cisco Cisco

Par la suite pour revenir à ce niveau du mode commande, il suffira de taper « CTRL+Z »

-----

### Entrer en configuration globale 
**Router #**

     configure terminal 
   
  ou   
  
    conf t  				                                                               

**Router(config) #** est le mode de configuration globale.

----

### Entrer en configuration interface

**Router(config) #**

    interface GigabitEthernet0/1/0  

0/1/0 à 0/1/3 pour les port LAN.


**(config-if)#** est le mode config interface 

----

### Configurer une adresse

    ip address  192.168.1.1 255.255.255.0              



----
###  Marquer l'interface comme étant connectée au réseau externe/public WAN.
     ip nat outside

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
 

