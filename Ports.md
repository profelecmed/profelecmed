# Ports

Les ports sont codés sur 16 bits, les puissances de 2 sont : 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16 384, 32 768, 65536


Il y a donc 65536 ports posibles.

### Les ports 0 à 1023 sont les ports réservés.
- 0      :             " Pour les protocoles TCP et UDP ce port est réservé.
- 20     :   FTP       " Data "
- 21     :   FTP       " Contrôle "
- 22     :   SSH       " Remplace, de manière sécurisée, Telnet "
- 23     :   Telnet    " Protocole de transport TCP "
- 25     :   SMTP      " Envoi de courrier "
- 53     :   DNS       " Domain Name System "
- 67     :   DHCP      " Les serveurs DHCP écoutent sur ce port les messages entrants des clients DHCP
- 68     :   DHCP      " Les clients DHCP utilisent ce pour envoyer des messages aux serveurs DHCP
- 80     :   HTTP      " Web "
- 80 : <span style="color:yellow;">HTTP</span> Web
- 110    :   POP3      " Réception de courrier "
- 143    :   IMAP      " Réception de courrier "
- 443    :   HTTPS     " http sécurisé par portions de SSL "
- 554    :   RTPS      ' Protocole de streaming temps-réel, exemple pour camera IP

### Les ports 1024 à 49151 sont les ports enregistrés.
- 1024 à 49151         " Ports enregistrés («Registered Ports») "
- 1723   :   PPTP      " Point-to-Point Tunneling Protocol ", utilisation VPN
- 3389   :   RDP       " Remote Desktop Protocol, protocole de bureau à distance "
- 8123   :   Home Assistant
- 8080   :             " Port utilisé par les proxy HTTP "

### Les ports 49152 à 65535 sont les ports dynamiques et/ou privés.
- 49152 à 65535        " Ports dynamiques et/ou privés («Dynamic and/or Private Ports») "

----

## Socket:

C'est la combinaison de l’adresse IP et du numéro de port.

voir pour plus de détails IANA :  Internet Assigned Numbers Authority    : https://www.iana.org

