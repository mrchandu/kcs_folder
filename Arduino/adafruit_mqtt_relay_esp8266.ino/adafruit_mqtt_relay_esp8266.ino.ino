
#include <ESP8266WiFi.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"

#define rel1 2 

#define WLAN_SSID       "kcs"
#define WLAN_PASS       "987654321"

#define AIO_SERVER      "io.adafruit.com"
#define AIO_SERVERPORT  1883                   // use 8883 for SSL
#define AIO_USERNAME    "kcsekhar"
#define AIO_KEY         "0fb06b8495c84600bafb2e213f3715b2"

WiFiClient client;
Adafruit_MQTT_Client mqtt(&client, AIO_SERVER, AIO_SERVERPORT, AIO_USERNAME, AIO_KEY);
Adafruit_MQTT_Subscribe high = Adafruit_MQTT_Subscribe(&mqtt, AIO_USERNAME "/feeds/high");
Adafruit_MQTT_Subscribe low = Adafruit_MQTT_Subscribe(&mqtt, AIO_USERNAME "/feeds/low");
void MQTT_connect();

void setup() {
  Serial.begin(115200);
  pinMode(rel1, OUTPUT);
  //digitalWrite(rel1,HIGH);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(WLAN_SSID);

  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.println("WiFi connected");
  Serial.println("IP address: "); 
  Serial.println(WiFi.localIP());

  // Setup MQTT subscription for onoff feed.
  mqtt.subscribe(&high);
  mqtt.subscribe(&low);
}

uint32_t x=0;

void loop() {
  MQTT_connect();
  Adafruit_MQTT_Subscribe *subscription;
  while ((subscription = mqtt.readSubscription(5000))) {
         // to test the tx line data
    if (subscription == &high){
      digitalWrite(rel1,HIGH);
    }
    if (subscription == &low){
      digitalWrite(rel1,LOW);
    }
  }
  if(! mqtt.ping()) {
    mqtt.disconnect();
  }
}

// Function to connect and reconnect as necessary to the MQTT server.
// Should be called in the loop function and it will take care if connecting.
void MQTT_connect() {
  int8_t ret;
  // Stop if already connected.
  if (mqtt.connected()) {
    return;
  }
 // Serial.print("Connecting to MQTT... ");
  uint8_t retries = 3;
  while ((ret = mqtt.connect()) != 0) { // connect will return 0 for connected
      // Serial.println(mqtt.connectErrorString(ret));
      // Serial.println("Retrying MQTT connection in 5 seconds...");
       mqtt.disconnect();
       delay(5000);  // wait 5 seconds
       retries--;
       if (retries == 0) {
         // basically die and wait for WDT to reset me
         while (1);
       }
  }
 // Serial.println("MQTT Connected!");
}
