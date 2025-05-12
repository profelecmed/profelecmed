# Configuration du NAT

🚩 Vous devez avoir fait les étpaes Commandes_1 et Commandes_2 afin de configurer en premier les adressees Inside et outside.
 ------

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
### Configuration NAT Static ,  Overload
   
Router(config)# 

Créer une Access-List pouur autorisé le réseau 192.168.100.0/24 

    ip access-list standard NAT_ACL permit 192.168.100.0 0.0.0.255

Overload permet pour plusieurs équipement interne d'avoir internet àtravers le routeur.

    ip nat inside source list NAT_ACL interface GigabitEthernet0/0/0/0 overload

    ip route 0.0.0.0 0.0.0.0 GigabitEthernet0/0/0
