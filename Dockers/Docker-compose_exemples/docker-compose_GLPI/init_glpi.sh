#!/bin/bash
sleep 10
# Configuration de la connexion à la base de données via la console GLPI
php /var/www/html/bin/console db:configure --db-host=db --db-name=glpidb --db-user=glpiuser --db-password=glpipassword -n

# Installation de la base de données GLPI via la console GLPI
php /var/www/html/bin/console db:install --reconfigure --force --default-language=fr_FR --db-host=db --db-name=glpidb --db-user=glpiuser --db-password=glpipassword -n

# Lancer Apache en arrière-plan
apache2-foreground
