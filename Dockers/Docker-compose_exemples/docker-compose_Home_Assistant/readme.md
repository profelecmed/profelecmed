# Home Assistant

Home Assistant est une solution domotique 


## Prérequis:
- Créer un dossier sur le bureau
- Nommer le dossier sans espace, Exemple docker_compose_home_assistant
- Copier vos fichiers
   - docker-compose.yml
- Dans le dossier faire MAJ + Clic droit puis cliquez sur Ouvrir la fenêtre PowerShell ici

## Etape 1 :
- Pour déployer votre application (Démarre vos services et conteneurs):

        docker-compose up --build -d
* ** --build** Force la reconstruction des images avant de démarrer les conteneurs.
* **-d** Exécute les conteneurs en arrière-plan, sans afficher leurs logs directement dans le terminal.


## Etape 2 :
* Ouvrir l’url:  http://localhost:8123
* ou   http://localhost:8123/onboarding.html
* Se reconnecter.
* Identifiant : glpi
* Mot de passe : glpi
