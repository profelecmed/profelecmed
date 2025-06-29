#  Fern Wi-Fi Cracker

🚩 Attention il est interdit d'accéder à des systèmes sans autorisation🏴‍☠️

### Mise en situation :

> Vous voulez pénétrer sur un réseau WLAN.
> 
> Le point d'accès demande une clès WEP ou WPA.

### Objectif :

✨ Vous devez casser la clè WEP ou WPA suivant le cas pour pénétrer dans un réseau Wi-Fi. 

-----

Support :

    PC Windows (Hôte)
    Kalilinux (par exemple en VM)
        Fern Wi-Fi Cracker
    Carte usb / Wifi
        driver cles wifi  Netgear WNA1100

Lz Wi-Fi, Wireless Fidelity est un réseaux sans-fil , c'est un WLAN pour Wireless Local Area Network.

# Prérequis
* Brancher la clès usb wifi
* Installer sur votre PC le driver pour la clès usb/WI-FI
* Vérifier dans le **Gestionnaire de périphérique** partie **Carte réseau** que **NETGEAR WNA1 ...** apparaît.

# Transfert de la carte USB/WI-FI à la VM Kalilinux
* Ouvrir Virtualbox, dans USB
    * ✔️ Controleur 3.0
    * Ajouter un filtre +
        Choisir :  **NETGEAR WNA1 ...** 
* Ouvrir Virtualbox, dans réseau choisir accès par pont
* Démarrer kalilinux
* Ouvrir la configuration réseau
* Authentification des données réseau (ssid et mot de passe)
* Vérification du réseau
    * Ouvrir le terminal

          ip &
> Vous devez avoir **wlan0 : flags ..........
> 
> > inet 192.168.1.XX

  # Méthode

## Etape 1 lancement :
* Rechercher dans kali Fern Wi-Fi Cracker
* Authentification admin
* Sélectionner l'interface à cibler **wlan0**
* Activer
* Détection des **Wi-Fi wep**
    * On obtient:
        > le ESSID
        >
        > le BSSID
        >
        > Le channel
        >
        > La puissance du signal
        >
        > Le cryptage 

Choisir l'étape 2 ou 3 suivant le type de clès WEP ou WPA


## Etape 2 si clè WEP:

Le protocole **WEP**, Wired Equivalent Privacy , norme internationale IEEE 802.11.

Le WEP utilise un algorithme de chiffrement à clé symétrique **RC4**
        
            
* Lancer le **Craking Encryption**

    * Choisir l'attaque **Regular** ou WPS

* Attendre , l'injection est en cours sur wlan0.

* Attendre ..... ...... ......

* Pendant l'attaque votre VM est déconnecté de votre réseau hôte.

> [!WARNING]
> Le WEP est maintenant obsolète!


## Etape 3 si clè WPA :

Le protocole **WPA** , Wi-Fi Protected Access


* Choisir une wordlist
wordlist
 
Nous allons utiliser un dictionnaire

rockyou
Vérifier la présence de rockyou dans le répertoire worklists. Le chemin est /usr/share/ferm ....

* Choisir une adresse MAC

* Lancer l'attaque Wi-Fi
* Attendre , l'injection est en cours sur wlan0.

> [!Note]
> Il y a le WPA2 qui améliore la sécurité avec l’algorithme de chiffrement très sécurisé AES , Advanced Encryption Standard.
>
> Maintenant il y a aussi le WPA3 , il utilise des procédés de chiffrement modernes SAE ; Simultaneous Authentication of Equals.
