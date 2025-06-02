# Exegol 
Exegol est une alternative a Kalilinux

## 0 Pré-requis
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

  🚩 si pas installé : https://git-scm.com/downloads/win
  
  Exemple ok : git version 2.49.0.windows.1

- Avoir docker

      docker --version
  
  Exemple ok : Docker version 28.0.1, build 068a01e


## 1 installation exegol
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
|  light | ~17.4GB |
|   osint | ~12.2GB |

Select an image by its name : 
- exemple **light**
- exegol install light

#### Vérification installation exegol

      python3 -m pip show exegol
      
#### Trouver le chemin d'accès

      python3 -m site --user-site

#### informations sur les images et conteneur 

      exegol info

   * version v4.3.11


|    Image tag    |   Size | Status |
|:-:    |:-:    |:-:    |
|  light | ~17.4GB | Up to date (V.3..6) |
| nightly | ~51.9GB | Not installed |
| web |  ~24.7GB | Not installed |
| ad |  ~40.0GB | Not installed |
|  full | ~51.7GB | Not installed |
|   osint | ~12.2GB| installed |

✖️ ici pas encore de conteneurs



## 2 installation image exegol

### installer une nouvelle image
- exemple image **osint**
  
      exegol install osint

#### informations sur les images et conteneur 

      exegol info

   * version 14.3.11


|    Image tag    |   Size | Status |
|:-:    |:-:    |:-:    |
|  light | ~17.4GB | Up to date (V.3..6) |
|   osint | ~12.2GB| Up to date (V.3..6) |
| nightly | ~51.9GB | Not installed |
| web |  ~24.7GB | Not installed |
| ad |  ~40.0GB | Not installed |
|  full | ~51.7GB | Not installed |


✖️ ici pas encore de conteneurs

## 3 Création conteneurs exegol

Conteneurs exegol en CLI ou environnement graphique

#### 3.1 Créer un nouveau conteneur en cli

Son nom est democonteneur

      exegol start democonteneurosint osint

#### 3.2 Créer un nouveau conteneur avec environnement graphique

Son nom est democonteneurgraph

      exegol start democonteneurosintgraph osint --desktop

- do you want exegol install one automaticaly ubuntu ? [Y:n]
- Choisir Y

- Enter new UNIX username:
- Choisir patron


|    Image tag    |   Size | Status |
|:-:    |:-:    |:-:    |
|  light | ~17.4GB | Up to date (V.3..6) |
|   osint | ~12.2GB| Up to date (V.3..6) |
| nightly | ~51.9GB | Not installed |
| web |  ~24.7GB | Not installed |
| ad |  ~40.0GB | Not installed |
|  full | ~51.7GB | Not installed |



On aura un lien vers localhost et un port. ainsi que l'id et mdp
