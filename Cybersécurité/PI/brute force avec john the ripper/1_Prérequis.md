# 1 Prérequis :

#### Mettre à jour le système.

* Ouvrit le terminal:

* Télécharge les dernières informations sur les paquets

       sudo apt update

* Télécharge et installe les nouvelles versions des paquets 

        sudo apt upgrade

#### Installer le démon **Snap**

       sudo apt install snapd

Redémarrer

       sudo reboot

#### Installer le snapd de **John the Ripper**

       sudo snap install john-the-ripper

#### Vérifier l'installation de **John the Ripper**

où est-il installé ?

       which john

Réponse possible si installé : /usr/bin/john
       
       apt list --installed | grep john



