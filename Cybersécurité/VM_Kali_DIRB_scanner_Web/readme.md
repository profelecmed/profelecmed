# Scanner de contenu Web , DIRB

DIRB  | Permet de lister les répertoires d’un site web

Support:

* VM : Kalolinux
  * DIRB


Le réseau :
* Nous allons utiliser dans notre exemple; Accès par pont

### Objectif
✨ Ici on va scanner un site WEB afin de déterminer ses répertoires. On va ensuite donner le flag trouvé.

### Pré-requis

* Vérifier si le site http://cielmed.free.fr est bien en ligne

  # Méthode

## Etape 1 lancement :
* Lancer la VM Kalilinux
* Rechercher dans kali , dirb
> $ dirb
>
> DIRB V2.22
>
> By The Dark Raver
>
> ...
> 

## Etape 3 Scanner le site:

dirb fait des recherches à partir de liste de mots.

* Se rendre dans le dossier wordlists de dirb

       cd  /usr/share/dirb/wordlists/

   * On va regarder les wordlists disponible dans dirb

         ls

      reponses:
       > small.txt
       >
       > big.txt
       >
       > ...
       > common.txt
       > 

*  Par défaut dirb utilise **common.txt** , regarder si common.txt contient flag.

      cat common.txt

* Lancer le scanne
  
      dirb http://cielmed.free.fr

* Réponses :
   > Scanning URL : http://cielmed.free.fr
   >
   > DIRECTORY
   >
   > + http://cielmed.free.fr/index.html
   >
   > + ... 


> [!TIP]
>
> Voir .htaccess
