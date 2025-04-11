# Docker

C'est une plateforme qui permet de créer, de déployer et de gérer des applications dans des conteneurs.

- **Télécharger :** Docker Desktop (on Windows) https://docs.docker.com/desktop/setup/install/windows-install/

- **Installionn :**
       - Installer Docker Desktop installer.exe
       - Cocher la case ✔️ Use WSL 2 instead of Hyper-V 
       - Cocher la case ✔️ AADD SHORTCUT TO DESKTO


- **Test initial :**

       Lancer le Docker Desktop
  
       Ouvrir le powershell

       Docker run hello world




- Dans le dossier faire **MAJ + Clic** droit puis cliquez sur Ouvrir la fenêtre PowerShell ici

## Vocabulaire docker

### Dockerfile
C'est un fichier texte contenant des instructionx afin de construire une image Docker.

### Image Docker
- Elle permet de créer un conteneur Docker avec (bibliothèques, dépendances,...) 

## Les commandes de bases Docker 

- A partir de Dockerfile on crée une image docker.

         docker build -t monimage .
  
- Créer et démarre un conteneur à partir d’une image.

         docker run hello-world

- Afficher toutes les commandes

         docker ls -a
