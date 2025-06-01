# GLPI
Application GLPI pour la gestion de parc informatique.


## Prérequis:
- Créer un dossier sur le bureau
- Nommer le dossier sans espace, Exemple docker_compose_glpi
- Copier vos fichiers
   - docker-compose.yml
   - Dockerfile
   - 000-default.conf
   - init_glpi.sh
- Dans le dossier faire MAJ + Clic droit puis cliquez sur Ouvrir la fenêtre PowerShell ici

## Etape 1 :
- Pour déployer votre application (Démarre vos services et conteneurs):

        docker-compose up --build -d

## Etape 2 :
* Ouvrir l’url:   http://localhost/index.php
* identifiant : glpi
* mot de passe : glpi
* init_glpi.sh

## Etape3 :
* Changement du mot de passe.
   * Noter le mot de passe administrateur du lab    
