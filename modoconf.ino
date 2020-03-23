//--------------------MODO_CONFIGURACION------------------------
void modoconf() {
  leds.setBrightness(100);
  leds.show();
  WiFi.softAP(ssidConf, passConf);
  IPAddress myIP = WiFi.softAPIP();

  Serial.print("IP del acces point: ");
  Serial.println(myIP);
  Serial.println("Modo AP...");

  server.on("/", paginaconf); //esta es la pagina de configuracion
  server.on("/guardar_conf", guardar_conf); //Graba en la eeprom la configuracion
  server.on("/escanear", escanear); //Escanean las redes wifi disponibles
  server.begin();
  while (true) {
    leds.setPixelColor(0, 255, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
    leds.setPixelColor(1, 255, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
    leds.show();
    delay(250);
    leds.setPixelColor(0, 0, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
    leds.setPixelColor(1, 0, 0, 0);   // cada pixel en color azul (posicion,R,G,B)}
    leds.show();
    delay(250);
    server.handleClient();
  }
}
