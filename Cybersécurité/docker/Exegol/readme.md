2exegol install
# Exegol 
Exegol est une alternative a Kalilinux

## Pré-requis
Voir la partie Dockers pour mise en place de docker sur votre machine.
- Avoir pyhton3

      python3 --version
  
  Exemple ok : Python 3.13.3

  🚩 Si ce n'est pas le cas sous windows on peut l'installer avec Microsoft Store : Python3.13

- Avoir pip

      pip --version
  
  Exemple ok : pip 25.1.1

   🚩 si pas à jour ,  A new release of pip is available: 24.3.1 -> 25.1.1

      python.exe -m pip install --upgrade pip

- Avoir git

      git--version
  
  Exemple ok : 

- Avoir docker

      docker --version
  
  Exemple ok : Docker version 28.0.1, build 068a01e


## Commandes
    python3 -m pip install exegol




installation exegol

    exegol install

### Available images

|    Image tag    |   Size |
 |:-:    |:-:    |
| nightly | ~51.9GB |
| web |  ~24.7GB |
| ad |  ~40.0GB |
|  full | ~51.7GB | 
|  ight | ~17.4GB |
|   osint | ~12.2GB |

Select an image by its name : 
- exemple **osint**
- exegol install osint

#### Vérification installation exegol

      python3 -m pip show exegol
      
#### Trouver le chemin d'accès

      python3 -m site --user-site

#### informations sur les images et container 
- exegol info

#### créer un nouveau conteneur
Son nom est democonteneur

- exegol start democonteneur osint

on peut avoir un environnement graphique. 

- exegol start democonteneur osint --desktop

On aura un lien vers localhost et un port. ainsi que l'id et mdp
