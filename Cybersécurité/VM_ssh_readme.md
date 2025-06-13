# SSH

Le réseau doit être en **Accès par pont**

Vérification si ssh sur la machine

    systemctl status ssh

* Exemple de non présence : unit ssh could not be found

Vérification si la commande est disponible:

    which ssh

* Si elle retourne le chemin alors elle est déjà installé.  /usr/bin/ssh


# installer openssh-server

mise à jour des dépot

    apt update

installatopn openssh-serveur
    
    apt install openssh-server


lancer la VM

Connection id et mdp

ouvrit un terminal

    su
mdp

    apt install ufw

Ajoutez une règle pour autoriser les connexions SSH :

    ufw allow 22/tcp

ufw enable


 ufw status
