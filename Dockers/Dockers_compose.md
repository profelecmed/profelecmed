# Docker Compose

**docker-compose.yml**, c'est le fichier de construction multi-conteneurs (des images Docker , Paramètrages , Réseau, ...). Utiliser pour les applications
qui comprennent plusieurs conteneurs.

## Dossier
Il est constituer de fichiers :
- **docker-compose.yml** , l'extension  **.yml** est pour un fichier **YAML** signifiant "Yet Another Markup Language", il regroupe les commandes pour lancer est configurer les différents conteneurs.
- **Dockerfile**
- ....

## Vocabulaire
- **Stack** , C'est un ensemble de services qui fonctionnent ensemble pour exécuter une
application.
- **Volume** , Permet de rendre les données du conteneur persistantes.


## Début
- Lancez le Docker Desktop

- Ouvrir le dossier contenant **docker-compose.yml**, 🚩 Il ne doit pas contenir d'espace, mettre un titre: titre_blabla_ok
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

