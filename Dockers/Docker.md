itls
# Docker

C'est une plateforme qui permet de créer, de déployer et de gérer des applications dans des conteneurs.

- **Télécharger :** Docker Desktop (on Windows) https://docs.docker.com/desktop/setup/install/windows-install/

---- 

 ## **Installation :**
- Installer Docker Desktop installer.exe
- Cocher les cases
   * ✔️ Use WSL 2 instead of Hyper-V
        ,  Cela va faire aparaître Linux "Windows Subsystem for Linux" dans l'explorateur de document.
   * ✔️ ADD SHORTCUT TO DESKTO
- Redémarrer le PC


## **Test initial :**

  - Lancer le Docker Desktop
  
   - Ouvrir le powershell , **MAJ + Clic**

Cette commande vous donnera des information sur la version de docker,   exemple : version 28.0.1    .... 

    docker --version

Vous devez voir : Hello from docker !   ,   This message shows that your installation appears to be working correctly
       
    Docker run hello-world  
 
Vous devez voir : root@fad23......:/#

    docker run -it ubuntu bash

Pour obtenir le aliste: 
  
    ls

la liste apparaît.

    exit

Vous êtes sortie d'ubuntu.


---- 

## Vocabulaire docker

### Dockerfile
C'est un fichier texte contenant des instructionx afin de construire une image Docker.

### Image Docker
- Elle permet de créer un conteneur Docker avec (bibliothèques, dépendances,...) 

### Conteneur docker
- C'est une application produite à partir d'une image docker.

## Les commandes de bases Docker 

- Dans le dossier faire **MAJ + Clic** droit puis cliquez sur Ouvrir la fenêtre PowerShell ici

- Pour obtenir de l'aide sur les commandes de docker.

      docker --help

- A partir de Dockerfile on crée une image docker.

         docker build -t monimage .
  
- Créer et démarre un conteneur à partir d’une image.

         docker run hello-world

- Afficher toutes les images

         docker images

- Afficher tous les containeurs

         docker ps -a
