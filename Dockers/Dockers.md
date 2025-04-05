# Docker

C'est une plateforme qui permet de créer, de déployer et de gérer des applications dans des conteneurs.

- Lancez le Docker Desktop

- Dans le dossier faire MAJ + Clic droit puis cliquez sur Ouvrir la fenêtre PowerShell ici

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

