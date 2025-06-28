#  Fern Wi-Fi Cracker

🚩 Attention il est interdit d'accéder à des systèmes sans autorisation🏴‍☠️

Support :

    PC Windows (Hôte)
    Kalilinux (par exemple en VM)
        Fern Wi-Fi Cracker
    Carte usb / Wifi
        driver cles wifi  Netgear WNA1100
# Prérequis
* Brancher la clès usb wifi
* Installer sur votre PC le driver pour la clès usb/WI-FI
* Vérifier dans le **Gestionnaire de périphérique** partie **Carte réseau** que **NETGEAR WNA1 ...** apparaisse.

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
        > Le cryptage , ici **WEP**
        >
        > le support , ici WPS
            
* Lancer le **Craking Encryption**

    * Choisir l'attaque **Regular** ou WPS

* Attendre , l'injection est en cours sur wlan0.

* Attendre ..... ...... ......

* Pendant l'attaque votre VM est déconnecté de votre réseau hôte.
  
