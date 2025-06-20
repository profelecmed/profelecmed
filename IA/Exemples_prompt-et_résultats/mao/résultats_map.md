# 🧠 Carte Mentale : Utilisation de Docker sous Windows

## 🖥️ Environnement de Travail
- Windows 10/11 avec WSL2 activé
- Docker Desktop installé
- Terminal : PowerShell / Terminal Windows

## 🔧 Outils et Interfaces
- **PowerShell**
  - Commandes de base Docker (`docker ps`, `docker run`, `docker stop`, etc.)
- **Portainer**
  - Interface graphique de gestion des conteneurs
  - Accès aux logs, stats, et gestion des volumes
- **Docker Compose**
  - Fichier `docker-compose.yml`
  - Gestion multi-services
  - Démarrage automatisé (`docker-compose up -d`)

## 🧪 Cas d'Usage : Déploiement de GLPI
- Services : `glpi`, `mariadb`, `phpmyadmin`
- Fichier `docker-compose.yml` :
  - Définition des services et ports
  - Volumes persistants
- Lancement : `docker-compose up -d`
- Accès : `http://localhost:port`

## 📦 Concepts Clés
- Conteneur vs Machine virtuelle
- Images Docker et `Dockerfile`
- Volumes (persistance des données)
- Réseaux Docker

## 🛠️ Bonnes Pratiques
- Nettoyage : `docker system prune`, `docker image rm`
- Sécurité : gestion des droits, suppression des conteneurs inutilisés
- Sauvegarde et restauration de volumes

## 📚 Ressources Complémentaires
- [Documentation officielle Docker](https://docs.docker.com/)
- [Portainer.io](https://www.portainer.io/)
- [GLPI Docker GitHub](https://github.com/pluginsGLPI/docker)
