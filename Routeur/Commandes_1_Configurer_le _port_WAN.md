# Commandes 1:

## Configurer le port WAN
                                                            
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

    interface GigabitEthernet0/0/0  

- 0/0/0 pour le port combo WAN   ou  0/0/1 pour le port WAN dédié.


**(config-if)#** est le mode config interface 

----

### Configurer une adresse
Router(config-if)#

1️⃣ Cas ou vous êtes en mode DHCP, permet d'obtenir l'adresse IP et la passerelle via DHCP
    
    ip address dhcp

2️⃣  Cas ou vous êtes en static

    ip address X.X.X.X  X.X.X.X              

Remùplacer l'adresse X.X.X.X  et le masque X.X.X.X par les valeurs données par le FAI ou de votre point d'access.

----
###  Marquer l'interface comme étant connectée au réseau externe/public WAN.
Router(config-if)#

     ip nat outside

----
### Activer l’interface
Router(config-if)#

    no shutdown

----
###  Quitter le mode de configuration interface 
Router(config-if)#

    exit

----
###  Quitter le mode de configuration  
Router(config)#

    exit

----
### Affiche les informations des interfaces
Router#

    show ip interface brief

----
### Sauvegarder votre configuration

 Router#

    write memory

  ou

    running-config startup-config
 

