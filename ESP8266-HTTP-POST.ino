#include <ESP8266WiFi.h>
#include <ArduinoJson.h>
#include <ESP8266HTTPClient.h>


const char* ssid = "TURBONETT_1C4362";
const char* password = "--------";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(100);
  }
  WiFi.mode(WIFI_STA);
}

void loop() {
  
  if(WiFi.status() == WL_CONNECTED){
    HTTPClient http;
    http.begin("http://192.168.1.16:5000/temp");
    http.addHeader("Content-Type", "application/json");
        
    String sJson = "";
    StaticJsonBuffer<200> jsonBuffer;
    JsonObject& root = jsonBuffer.createObject();
    
    root["id"] = 0;
    root["tempvalue"] = map(analogRead(A0), 0, 1023, 0, 100);
    root["tempdate"] = "now";
    root.printTo(sJson);
    
    int httpCode = http.POST(sJson);
    String payload = http.getString();

    Serial.println(sJson);
    Serial.print("httpCode = ");
    Serial.print(httpCode);
    Serial.print("  payload = ");
    Serial.println(payload);    

    http.end();

    delay(10000);
  }else{
    Serial.println("WiFi no conectado");
    delay(1000);
  }

}
