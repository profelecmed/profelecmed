#include <WiFi.h>
#include <WebServer.h>
#include <LittleFS.h>

// Définition du nom du réseau Wi-Fi (SSID) et du mot de passe
const char* ssid = "Mon_ESP32_WiFi";
const char* password = "SuperMotDePasse123"; // 8 caractères minimum (ou "" pour un réseau ouvert)

WebServer server(80);

// Fonction pour déterminer le type de fichier (MIME type)
String getContentType(String filename) {
  if (filename.endsWith(".html")) return "text/html";
  if (filename.endsWith(".css")) return "text/css";
  if (filename.endsWith(".js")) return "application/javascript";
  if (filename.endsWith(".png")) return "image/png";
  if (filename.endsWith(".jpg")) return "image/jpeg";
  if (filename.endsWith(".ico")) return "image/x-icon";
  return "text/plain";
}

// Fonction pour lire un fichier depuis LittleFS et l'envoyer au navigateur
bool handleFileRead(String path) {
  // Si on demande la racine, on redirige vers index.html
  if (path.endsWith("/")) {
    path += "index.html";
  }
  
  String contentType = getContentType(path);
  
  if (LittleFS.exists(path)) {
    File file = LittleFS.open(path, "r");
    server.streamFile(file, contentType);
    file.close();
    return true;
  }
  return false; // Fichier non trouvé
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  // 1. Initialisation de LittleFS
  if (!LittleFS.begin(true)) {
    Serial.println("Erreur lors du montage de LittleFS...");
    return;
  }
  Serial.println("LittleFS monté avec succès.");

  // 2. Configuration de l'ESP32 en Point d'Accès (AP)
  Serial.print("Configuration du Point d'Accès... ");
  WiFi.softAP(ssid, password);

  IPAddress myIP = WiFi.softAPIP();
  Serial.print("Prêt ! Adresse IP du serveur : ");
  Serial.println(myIP); // Par défaut, ce sera souvent 192.168.4.1

  // 3. Gestion des requêtes HTTP
  // Si le fichier demandé n'est pas explicitement défini, on cherche dans LittleFS
  server.onNotFound([]() {
    if (!handleFileRead(server.uri())) {
      server.send(404, "text/plain", "Fichier non trouvé sur l'ESP32.");
    }
  });

  server.begin();
  Serial.println("Serveur HTTP démarré.");
}

void loop() {
  server.handleClient();
}
