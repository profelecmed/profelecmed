# Dockerfile :  hello les CIEL

# Utilisation d'une image minimale basée sur Alpine
FROM alpine:latest

# Création d'un script de test avec le message modifié
RUN echo -e '#!/bin/sh\necho "Hello les CIEL"' > /hello && chmod +x /hello

# Définition de la commande par défaut
CMD ["/hello"]
