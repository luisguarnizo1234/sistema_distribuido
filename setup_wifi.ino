

void setup_wifi() {

  //------------------------ SETUP WIFI -----------------------------

  WiFi.mode(WIFI_STA); WiFi.begin(ssid, pass);
  Serial.println("CONECTANDO A INTERNET");
  leds.setBrightness(100);

  while (WiFi.status() != WL_CONNECTED and contconexion < 50) { // CONEXION CON LA RED PARA EL ANALISIS
    ++contconexion;
    Serial.print(".");
    leds.setPixelColor(0, 0, 0, 255);   // cada pixel en color azul (posicion,R,G,B)}
    leds.setPixelColor(1, 0, 0, 255);   // cada pixel en color azul (posicion,R,G,B)}
    leds.show(); delay(250);
    leds.setPixelColor(0, 0, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
    leds.setPixelColor(1, 0, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
    leds.show(); delay(250);
  }

  if (contconexion < 50) {
    Serial.print(" WIFI CONECTADO "); Serial.println(WiFi.localIP());
    contconexion = 0;

    ///--------------------- CONECCION AL SERVIDOR MQTT ----------------

    client.setServer(IPservidor, mqttPort);
    Serial.println("CONECTANDO A MQTT");
    leds.setBrightness(100);

    while (!client.connected() and contconexion < 10) {    // CONEXION CON EL SERVIDOR
      ++contconexion;
      Serial.print(".");
      for (i = 0; i < 8; i++) {
        leds.setPixelColor(0, 0, 255, 0);   // cada pixel en color azul (posicion,R,G,B)}
        leds.setPixelColor(1, 0, 255, 0);   // cada pixel en color azul (posicion,R,G,B)}
        leds.show();
        delay(200);
        leds.setPixelColor(0, 0, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
        leds.setPixelColor(1, 0, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
        leds.show();
        delay(200);
      }
      
      if (client.connect(Nodo)) {
        delay(100);
      }
      
    }

    if (contconexion < 10) {

      Serial.print(" SERVIDOR CONECTADO "); Serial.println(IPservidor);
      contconexion = 0;
      for (i = 0; i < 8; i++) {
        leds.setPixelColor(0, 87, 35, 100);   // cada pixel en color azul (posicion,R,G,B)}
        leds.setPixelColor(1, 87, 35, 100);   // cada pixel en color azul (posicion,R,G,B)}
        leds.show();
        delay(250);
        leds.setPixelColor(0, 0, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
        leds.setPixelColor(1, 0, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
        leds.show();
        delay(250);
      }

    } else {
      Serial.println("ERROR AL CONECTAR A MQTT");
      for (i = 0; i < 8; i++) {
        leds.setPixelColor(0, 255, 128, 0);   // cada pixel en color azul (posicion,R,G,B)}
        leds.setPixelColor(1, 255, 128, 0);   // cada pixel en color azul (posicion,R,G,B)}
        leds.show();
        delay(250);
        leds.setPixelColor(0, 0, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
        leds.setPixelColor(1, 0, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
        leds.show();
        delay(250);
      }
      delay(1000);
      ESP.restart();
    }

  } else {
    Serial.println("ERROR AL CONECTAR A INTERNET");
    for (i = 0; i < 8; i++) {
      leds.setPixelColor(0, 255, 128, 0);   // cada pixel en color azul (posicion,R,G,B)}
      leds.setPixelColor(1, 255, 128, 0);   // cada pixel en color azul (posicion,R,G,B)}
      leds.show();
      delay(250);
      leds.setPixelColor(0, 0, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
      leds.setPixelColor(1, 0, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
      leds.show();
      delay(250);
    }
    delay(1000);
    ESP.restart();
  }
}
