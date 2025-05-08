# Commandes:

## Attribution Gigabit Ethernet Interfaces
                                                            
### Entrer en mode privilégié 
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

    interface GigabitEthernet0/0/0  

- 0/0/0 pour le port combo WAN   ou  0/0/1 pour le port WAN dédié.
- 0/1/0 à 0/1/3 pour les port LAN

----

----
### Affiche les informations des interfaces

    show ip interface brief
  
  
 

