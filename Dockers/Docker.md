# Docker

C'est une plateforme qui permet de créer, de déployer et de gérer des applications dans des conteneurs.
Il permet de packager des applications avec leurs dépendances.

- **Télécharger :** Docker Desktop (on Windows) https://docs.docker.com/desktop/setup/install/windows-install/

---- 

 ## **Installation :**
- Installer Docker Desktop installer.exe
- Cocher les cases
   * ✔️ Use WSL 2 instead of Hyper-V
        ,  Cela va faire aparaître Linux "Windows Subsystem for Linux" dans l'explorateur de document.
   * ✔️ ADD SHORTCUT TO DESKTO
- Cliquer afin de lancer l'installation de WSL si nécessaire.
- Redémarrer le PC


## **Test initial :**

  - Lancer le Docker Desktop
  
   - Ouvrir le powershell , **MAJ + Clic**

- Obtenir les informations sur la version de docker avec la commande version :

      docker --version
    Exemple : version 28.0.1    .... 


- test du conténeur Hello Word:
         
      Docker run hello-world  
 
     Vous devez voir : Hello from docker !   ,   This message shows that your installation appears to be working correctly

- Test du conteneur ubuntu:

      docker run -it ubuntu bash
     Vous devez voir : root@fad23......:/#

     Pour obtenir la liste: 
  
      ls

     la liste apparaît. " bin boot dev etc home lib media opt root... sys tmp usr var"

     Por sortir de ubuntu
  
      exit

     Vous êtes sortie d'ubuntu.


---- 

## Vocabulaire docker

### Dockerfile
- docker help
- C'est un fichier texte contenant des instructionx afin de construire une image Docker.

### 🖼️ Image Docker
- Elle permet de créer un conteneur Docker avec (bibliothèques, dépendances,...) 

### 🈴Conteneur docker
- C'est une application produite à partir d'une image docker.

## Les commandes de bases Docker 

- Dans le dossier faire **MAJ + Clic** droit puis cliquez sur Ouvrir la fenêtre PowerShell ici

- Pour obtenir de l'aide sur les commandes de docker.

      docker --help

- Télécharger une image docker depuis un dépot "ici Kalilinux en version rolling release"

         docker pull kalilinux/kali-rolling

- A partir de Dockerfile on crée une image docker.

         docker build -t monimage .
  
- Créer et démarre un conteneur à partir d’une image.

         docker run hello-world

- Afficher toutes les images

         docker images

- Supprimer une image

         docker rmi hello-world


- Afficher tous les conteneurs

         docker ps -a
  
- Arrêter un conteneur

         docker stop hello-world

- Démarrer un conteneur

         docker start hello-world

- Supprimer un conteneur

         docker rm hello-world
