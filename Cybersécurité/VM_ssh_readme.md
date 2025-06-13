# SSH

Le réseau doit être en **Accès par pont**

Vérification si ssh sur la machine

    systemctl status ssh

Exemple de non présence : unit ssh could not be found

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
