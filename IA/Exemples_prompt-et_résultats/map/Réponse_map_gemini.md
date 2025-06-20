Compris ! Voici une carte mentale au format Markdown sur votre cours Docker sous Windows, spécialement conçue pour vos élèves de Bac Pro CIEL.

---

## Carte Mentale : Docker sous Windows - Gestion de Conteneurs

---

### **1. Introduction à Docker**

* **Qu'est-ce que Docker ?**
    * Plateforme de conteneurisation
    * Permet d'isoler des applications et leurs dépendances
    * Simplifie le déploiement et la portabilité
* **Pourquoi Docker ?**
    * Environnements cohérents (développement, test, production)
    * Moins de problèmes de compatibilité
    * Optimisation des ressources
    * Déploiement rapide

---

### **2. Installation et Configuration sous Windows**

* **Prérequis**
    * Windows 10 Pro/Entreprise/Éducation (ou Windows Server)
    * Hyper-V activé
    * WSL 2 (Windows Subsystem for Linux 2) recommandé
* **Installation de Docker Desktop**
    * Téléchargement depuis le site officiel Docker
    * Assistant d'installation simple
* **Vérification de l'installation**
    * `docker version`
    * `docker info`

---

### **3. L'Interface Ligne de Commande (CLI) - PowerShell**

* **Commandes Docker Essentielles**
    * `docker pull [image]` : Télécharger une image
    * `docker images` : Lister les images locales
    * `docker run [options] [image] [commande]` : Lancer un conteneur
        * `-d` : Détaché (en arrière-plan)
        * `-p [port_hôte]:[port_conteneur]` : Mappage de ports
        * `--name [nom]` : Nommer le conteneur
        * `-v [volume_hôte]:[volume_conteneur]` : Monter un volume
    * `docker ps` : Lister les conteneurs en cours d'exécution
    * `docker ps -a` : Lister tous les conteneurs (y compris arrêtés)
    * `docker stop [ID/nom]` : Arrêter un conteneur
    * `docker start [ID/nom]` : Démarrer un conteneur
    * `docker restart [ID/nom]` : Redémarrer un conteneur
    * `docker rm [ID/nom]` : Supprimer un conteneur
    * `docker rmi [ID/nom]` : Supprimer une image
    * `docker logs [ID/nom]` : Afficher les logs d'un conteneur
    * `docker exec -it [ID/nom] [commande]` : Exécuter une commande dans un conteneur (ex: `bash`)

---

### **4. Gestion Visuelle avec Portainer**

* **Qu'est-ce que Portainer ?**
    * Interface utilisateur graphique (GUI) pour Docker
    * Simplifie la gestion des conteneurs, images, volumes, réseaux
* **Installation de Portainer**
    * Déploiement en tant que conteneur Docker :
        ```bash
        docker volume create portainer_data
        docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
        ```
* **Fonctionnalités Clés**
    * Tableau de bord (vue d'ensemble)
    * Gestion des conteneurs (démarrer, arrêter, redémarrer, logs, exec)
    * Gestion des images (pull, build, supprimer)
    * Gestion des volumes et réseaux
    * Création de Stacks (Docker Compose)

---

### **5. Docker Compose pour les Applications Multi-Conteneurs**

* **Concept de Docker Compose**
    * Outil pour définir et exécuter des applications Docker multi-conteneurs
    * Utilise un fichier YAML (`docker-compose.yml`)
* **Fichier `docker-compose.yml`**
    * Définition des services (conteneurs)
    * Ports, volumes, réseaux, dépendances
    * Exemple (simplifié pour GLPI) :
        ```yaml
        version: '3.8'
        services:
          db:
            image: mariadb:10.5
            environment:
              MYSQL_ROOT_PASSWORD: my_secret_password
              MYSQL_DATABASE: glpidb
              MYSQL_USER: glpiuser
              MYSQL_PASSWORD: glpipassword
            volumes:
              - db_data:/var/lib/mysql
          glpi:
            image: diouxx/glpi:latest
            depends_on:
              - db
            ports:
              - "80:80"
            environment:
              GLPI_DATABASE_HOST: db
              GLPI_DATABASE_NAME: glpidb
              GLPI_DATABASE_USER: glpiuser
              GLPI_DATABASE_PASSWORD: glpipassword
            volumes:
              - glpi_data:/var/www/html/glpi
        volumes:
          db_data:
          glpi_data:
        ```
* **Commandes Docker Compose**
    * `docker-compose up -d` : Démarrer l'application en arrière-plan
    * `docker-compose down` : Arrêter et supprimer les conteneurs
    * `docker-compose ps` : Statut des services
    * `docker-compose logs` : Afficher les logs de tous les services

---

### **6. Exemple Pratique : Déploiement de GLPI avec Docker Compose**

* **GLPI** : Gestion Libre de Parc Informatique
* **Architecture Conteneurisée**
    * Conteneur pour la base de données (MariaDB/MySQL)
    * Conteneur pour l'application GLPI (serveur web + PHP)
* **Étapes Clés**
    1.  Création du fichier `docker-compose.yml` (comme ci-dessus)
    2.  Lancement avec `docker-compose up -d`
    3.  Accès à GLPI via le navigateur (ex: `http://localhost`)
    4.  Finalisation de l'installation de GLPI via l'interface web
    5.  Gestion et maintenance (logs, redémarrage)

---

### **7. Concepts Avancés & Bonnes Pratiques (Introduction)**

* **Volumes** : Persistance des données
* **Réseaux Docker** : Communication entre conteneurs
* **Dockerfiles** : Construire ses propres images
* **Sécurité des Conteneurs**
* **Orchestration** (Kubernetes - pour plus tard !)

---

J'espère que cette carte mentale aidera vos élèves à structurer leurs connaissances et à mieux visualiser les concepts abordés ! N'hésitez pas si vous avez d'autres besoins.
