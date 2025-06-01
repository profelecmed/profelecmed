# Dockerfile :  hello les CIEL
# Fichier de personnalisation de l'image

# Sert à spécifier l'image de basée qui va être utilisé ici c'est l'image de Alpine
FROM alpine:latest

# Run permet de lancer une commande ici création d'un script de test avec le message modifié
RUN echo -e '#!/bin/sh\necho "Hello les CIEL"' > /hello && chmod +x /hello

# Définition de la commande par défaut, programme éxecuté au lancement du conteneur
CMD ["/hello"]
