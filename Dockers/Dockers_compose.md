# Docker Compose

**docker-compose.yml**, c'est le fichier de construction multi-conteneurs (des images Docker , Paramètrages , Réseau, ...)

- Lancez le Docker Desktop

- Dans le dossier faire **MAJ + Clic** droit puis cliquez sur **Ouvrir la fenêtre PowerShell ici** , Il faut être dans le bon répertoire!
                  ...../.../.../monrépertoire#

## Les commandes de bases Docker Compose:

- Pour connaitre la version:

        docker-compose --version
    Exemple : Docker Compose version V2.33.1-destokp.1

- Pour déployer votre application (Démarre vos services et conteneurs):

        docker-compose up

- Pour arrêter tous les services et conteneurs:
    
        docker-compose down

- Pour redémarrer: 
 
        docker-compose restart

 - Pour afficher les conteneurs en cours d'éxecution:
 
        docker-compose ps

