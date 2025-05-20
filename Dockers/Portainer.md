# Portainer

 Portainer permet dedéployer, de gérer et de surveiller vos conteneurs avec une interface graphique.

### Prérequis:

- Installation de Docker
- **Installation de Portainer** , utiliser le docker-compose dans le répertoire **docker-compose_portainer**
  - Pour déployer votre application (Démarre vos services et conteneurs):

        docker-compose up -d
     -d afin d'éxécuter le conteneur en mode détaché.

### Accéder à l’interface web Portainer en local

* Dans votre navigateur

      http://localhost:9000
Créer votre compte admin , mettre notre mot de passe pour le lab pour l'adminstrateur.

#### Utilisations

-  Cliquez sur **Environnement-related** puis **Environnements**
-  Cliquez sur le docker **local** , il apparaît le menu image doicker **local**
-  Cliquez sur **Templates** puis choisir votre application à installer par exemple **Gitlab CE**
