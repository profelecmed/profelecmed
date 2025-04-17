# Site web CIEL

## Etape 1 
* Créer un dossier sur le bureau
* Nommer le dossier sans espace,     Exemple **htmlciel**
* Copier vos fichiers
   ** dockerfile
   ** index.html

## Etape 2
sous windows:
* Lancer Docker Descktop

## Etape 3
* Ouvrir le powershell , MAJ + Clic
- A partir de Dockerfile on crée une image docker.

         docker build -t htmlciel .
  
- Créer et démarre un conteneur à partir d’une image.

         docker run -d -p 8080:80 htmlciel

# Etape 4
* Ouvrir l’url:   http://localhost:8080/
