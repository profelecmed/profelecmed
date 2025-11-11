# Protocoles:

- Modèle **TCP/IP**  : 4 Couches :  
  * 4  Application
  * 3  Transport
  * 2  Internet
  * 1  Accès réseau
  
- Modèle **OSI**     : 7 Couches :   Open Systems Interconnexion 
   * 7  Application
   * 6  Présentation
   * 5  Session 
   * 4  Transport
   * 3  Réseau
   * 2  Liaison de données
   * 1  Physique


## A
- **ARP**            :  Address Resolution Protocol            : Permet d'obtenir par une requête l'adresse MAC correspondant à l’adresse IP.
## D
- **DHCP**           :  Dynamic Host Configuration Protocol.   : Configuration automatique des paramètres IP
  - Phase 1 : DHCPDISCOVER
  - Phase 2 : DHCPOFFER
  - Phase 3 : DHCPREQUEST
  - Phase 4 : DHCPACK  

- **DNS**            :  Domain Name System                     : Association noms et IP
  - Google:   En IPV4: - DNS Primaire:  8.8.8.8  ,   :  - DNS Primaire:       8.8.4.4   
  - Cloudflare:  En IPV4:  : classique, sans blocage : - DNS Primaire:  1.1.1.1 ,  - DNS secondaire :  1.0.0.1
  - Cloudflare:  En IPV4: : blocage malwares : - DNS Primaire:  1.1.1.2 ,  - DNS secondaire :  1.0.0.2
  - Cloudflare:  En IPV4: : blocage malwares et adulte : - DNS Primaire:  1.1.1.3 ,  - DNS secondaire :  1.0.0.3
  - Google:   En IPV6: - DNS Primaire: 2001:4860:4860::8888  ,   :  - DNS Primaire:      2001:4860:4860::8844  


## F
- **FTP**            :  File Transfer Protocol                 : Protocole de transfert de fichiers
##  H
- **HTTP**           :  Hypertext Transfer Protocol
 *  HTTP Métodes   :
      *  GET   : Pour récupérer des données de la page web
      *  HEAD  : Pour récupérer les informatons de l'en-tête de la page web
      *  POST  : Pour créer une ressource
      *  PUT   : Pour mettre à jour une ressource
   *  HTTP Status Codes   :
      *  200 🏷️ OK
      *  404 🔖 The server has not found
      *  503 🔖 Service Unavailable
- **HSRP**           :  Hot Standby Router Protocol            : Protocole Cisco de gestion de routeurs avec un prioritaire 
## I
- **ICMP**           :  Internet Control Message Protocol      : Détection des erreurs lors de transmission en TCP/IP, "Commande: ping"
- **IMAP**           :  Internet Message Access Protocol       : Opposé au POP. Ici on consulte ses mails sur le serveur dirrectement.
- **IP**             :  Internet Protocol                      : IPv4 ou IPv6
  - **IPv4** , La taille de l'adresse IPv4 est de 32 bits
    - IP/24 pour un masque 255.255.255.0
  - **IPv6** , La taille de l'adresse IPv6 est de 128 bits
    -    Adresse de bouclage      **::1**    Localhost
    -    Adresses unicast & routables sur internet **2000::/3 à 3FFF**
    -    Adresses locales uniques **FC00::/7 et FDFF::/7.**
    -    Adressees locales lien , link-local     **fe80::/10**
    -    Adresses multicast **FF00::/8**  , Adresses de groupes pour la communication multicast

## L
- **LACP**           :  Link Aggregation Control Protocol      : Niveau 2de OSI.
- **LDAP**           :  Lightweight Directory Access Protocol  : Il est utilisé pour l’authentification des services d’annuaire, type AD
## M
- **MQTT**           :  Message Queuing Telemetry Transport    : Transmission de données IoT
     -  Broker |  Clients  | Messages  
## N
- **NDP**            : Neighbor Discovery Protocol             : Remplace ARPpour IPv6 et intègre des fonctions de sécurité.
- **NTP**            :  Network Time Protocol                  : Protocole de synchronisation de réseau
## P
- **POP3**           :  Post Office Protocol                   : Il permet de télécharger et stosk en local des e-mails d'un serveur vers un client  
- **PPPoE**          :  point-to-point protocol over Ethernet  : Créer un tunnel de niveau 2 entre deux routeurs
- **PPTP**           :  Point-to-Point Tunneling Protocol      : Utilisation VPN, ce protocole est obsolète et vulnérable.
## R
- **RARP**           :  Reverse Address Resolution Protocol    : Inverse de ARP
- **RDP**            :  Remote Desktop Protocol                : Bureau à distance avec le port port réseau 3389 
- **RIP**            :  Routing Information Protocol           : C’est un protocole d'information de routage.
- **RSTP**           :  Rapid Spanning Tree Protocol           : Il détecte les topologies afin d’assurer une convergence plus rapide et sans boucles
- **RTP**            :  Real Time Transport Protocol           : Conçu plutôt pour audio et vidéo
## S
- **SIP**            :  Session Initiation Protocol            : Sessions "d'appel" multimédia.
- **SFTP**           :  SSH FTP ou Secure FTP                  : utilise un canal sécurisé pour transférer des fichiers.
- **SMTP**           :  Simple Mail Transfer Protocol          : Il est utilisé pour transférer le courrier électronique
- **SOAP**           :  Simple Object Access Protocol          :  est un protocole de messagerie permettant d'échanger des informations structurées dans des services Web, utilisé par les API.
- **Spanning-Tree**  :                                         : créer un chemin logique unique dans une architecture redondante.
- **SPX**            :  Sequenced Packet Exchange              : Protocole de transmission qui est remplacé par TCP / IP.
- **SSH**            :  Secure Shell                           : Sessions , transfert de fichiers de manière sécurisée
- **SSL**            :  Secure Sockets Layer                   : Voir maintenant le protocole TLS.
## T
- **Telnet**         :  TErminaL NETwork protocol              : Attention transmission en clair!
- **TCP**            :  Transport Control Protocol             : Transmission de données fiable , détection et une correction d’erreurs
- **TLS**            :  (Transport Layer Security              : Successeur du protocole SSL il a pour objectif le Chiffrement , l'authentification et la vérificatin de l'intégrité


## U
- **UDP**            :  User Datagram Protocol                 : Transmission de datagrammes sans connection.
## V
- **VRRP**           :  Virtual Router Redundancy Protocol     : Il utilise une adresse IP virtuelle référençant un groupe de routeurs.
- **VoIP**           :  Voice over Internet Protocol           : Voix sur IP, utilisation pour la téléphonie
- **VVoIP**          :  Voice and Video over Internet Protocol 
- **VTP**            :  VLAN Trunking Protocol
## W
- **WinRM**          :  Windows Remote Management              : Service Microsoft qui permet la gestion à distance sécurisée des serveurs Windows 
- **WireGuard**      :  Protocole VPN                          : Autres (IPsec, OpenVPN)
