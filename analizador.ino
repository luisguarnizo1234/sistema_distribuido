
void analizador() {
  n = WiFi.scanNetworks();
  if (n == 0) {
    Serial.println("NO HAY REDES DISPONIBLES");
  } else {
    escan();
    ruido = ruido - senal;
    rui = ruido;
    rui =  10 * (log10 (rui));     //// ruido en dBm

    senal = senal * 1000000;
    ruido = ruido * 1000000;

    SNR = senal / ruido;
    dbm =  10 * (log10 (SNR));
    ruido = 0;
  }
}
