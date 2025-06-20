# GameShell

## Etape 1 
* Créer un dossier sur le bureau
* Nommer le dossier sans espace,     Exemple **gamshellciel**
* Copier vos fichiers
  * dockerfile
 
  ![Docker_rep_webciel](https://github.com/profelecmed/profelecmed/blob/main/pictures/docker_html_ciel.jpg)

## Etape 2
sous windows:
* Lancer Docker Descktop

## Etape 3
* Ouvrir le powershell , MAJ + Clic
- A partir de Dockerfile on crée une image docker.

         docker build -t gameshellciel .
  
- Créer et démarre un conteneur à partir d’une image.

         docker run -d -p 8080:80 gameciel
