# Docker

C'est une plateforme qui permet de créer, de déployer et de gérer des applications dans des conteneurs.

- **Télécharger :** Docker Desktop (on Windows) https://docs.docker.com/desktop/setup/install/windows-install/


 ## **Installation :**
- Installer Docker Desktop installer.exe
- Cocher la case ✔️ Use WSL 2 instead of Hyper-V (Cela va Dans l'explorateur de document faire aparaître Linux "Windows Subsystem for Linux)
- Cocher la case ✔️ ADD SHORTCUT TO DESKTO
- Redémarrer le PC


## **Test initial :**

  - Lancer le Docker Desktop
  
   - Ouvrir le powershell , **MAJ + Clic**

    docker --version

Cette commande vous donnera des information sur la version de docker,   exemple : version 28.0.1    .... 
       
    Docker run hello-world  
 
  Vous devez voir : Hello from docker !   ,   This message shows that your installation appears to be working correctly

    docker run -it ubuntu baSh

Vous devez voir : root@fad23......:/#

    ls

la liste apparaît.

    exit

Vous êtes sortie d'ubuntu.


- Dans le dossier faire **MAJ + Clic** droit puis cliquez sur Ouvrir la fenêtre PowerShell ici



## Vocabulaire docker

### Dockerfile
C'est un fichier texte contenant des instructionx afin de construire une image Docker.

### Image Docker
- Elle permet de créer un conteneur Docker avec (bibliothèques, dépendances,...) 

## Les commandes de bases Docker 

- Pour obtenir de l'aide sur les commandes de docker.

      docker --help

- A partir de Dockerfile on crée une image docker.

         docker build -t monimage .
  
- Créer et démarre un conteneur à partir d’une image.

         docker run hello-world

- Afficher toutes les commandes

         docker ls -a
