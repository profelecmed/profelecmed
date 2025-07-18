https://markmap.js.org/repl

On colle par exemple:

# Docker sous Windows 🐳💻
- PowerShell 📜
  - Lancement de Docker
  - Commandes de base
    - docker version
    - docker ps, docker ps -a
    - docker run
    - docker stop / start / rm
    - docker images, docker rmi
- Docker Desktop 🖥️
  - Interface graphique
  - Paramètres & intégration système
  - Accès aux logs, volumes, réseaux
- Portainer 🧭
  - Interface web pour Docker
  - Déploiement de Portainer
    - docker volume create portainer_data
    - docker run -d -p 9000:9000 ...
  - Gestion des containers / images
  - Surveillance en temps réel
- docker-compose 🧩
  - Définition de services en YAML
  - Commandes :
    - docker-compose up -d
    - docker-compose down
  - Gestion multi-container
- Exemple pratique : GLPI 🗃️
  - GLPI + MariaDB avec docker-compose
  - Arborescence projet :
    - docker-compose.yml
    - Volumes pour persistance
  - Accès via navigateur : http://localhost:8080
- Compétences visées 🎯
  - Compréhension des containers
  - Autonomie dans le déploiement de services
  - Utilisation d'interfaces d'administration (Portainer)
  - Notions de virtualisation légère
- Bonnes pratiques ✔️
  - Nettoyage des ressources inutiles : docker system prune
  - Utilisation des volumes
  - Sécurisation des accès web
- Ressources complémentaires 📚
  - https://docs.docker.com/
  - https://github.com/docker-glpi
  - https://www.portainer.io/


![mapdocker](https://github.com/profelecmed/profelecmed/blob/main/pictures/map_dockere.jpg) 

