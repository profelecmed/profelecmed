# Metasploitable2

C'est une machine virtuelle pour votre LAB sur la cybersécurité, elle est basée sur Linux.
Elle est intentionnellement vulnérable afin de pouvoir tester des attaques. 

* Se rendre sur le site  :  https://sourceforge.net/projects/metasploitable/
* Télécharger



## Création de la VM sosu VirtualBox:

* Nouvelle
* Name and Operating System
  * Non : Linux_lab_vulnerable
  * Type : Linux
  * Subtype : Debian
* Hard Disk :
*  Use an existing Virtual Hard Disk File
 *  Ajouter  : Sélectionner le chemin pour Metasploitable.vmdk 

## Démarrage

* username **msfadmin**
* password **msfadmin**.
  
🚩 Le clavier est en querty

Pour obtenir un clavier Français

    sudo loadkeys fr

## Tests:

Déterminer l'adresse IP:

    ifconfig

Plus moderne

    ip a
adresse IP : 10.0.2. XX

Ensuite la table de routage

    route

La passerelle est 10.0.2. YY

-----
> Metasploitable 2 Exploitability Guide
>
> https://docs.rapid7.com/metasploit/metasploitable-2-exploitability-guide/
