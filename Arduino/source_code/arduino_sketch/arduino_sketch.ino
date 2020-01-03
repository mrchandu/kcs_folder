

/*
   IoT - Remotely control 220-240V bulb with NodeMCU through MQTT broker
*/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const int relayPin = D0;
const char* mqttServerURL = "iot.eclipse.org";
const char* mqttTopic = "/lamp/status/";

// Update these with values suitable for your network.
const char* ssid = "*********************************";
const char* password = "*****************************";

WiFiClient espClient;
PubSubClient mqttClient(espClient);

void setup()
{
  Serial.begin(115200);

  setupWifi();

  mqttClient.setServer(mqttServerURL, 1883);
  mqttClient.setCallback(callback);

  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, HIGH);
}

void loop()
{
  if (!mqttClient.connected())
  {
    connectToMQTT();
  }

  mqttClient.loop();
}

void setupWifi()
{
  delay(100);

  // We start by connecting to a WiFi network
  Serial.print("Connecting to: ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length)
{
  Serial.print("Command from MQTT broker is : ");
  Serial.print(topic);

  bool turnOnRelay = payload[0] == '1';
  if (turnOnRelay)
  {
    digitalWrite(relayPin, LOW);
    Serial.println(" Device On! " );
  }
  else
  {
    digitalWrite(relayPin, HIGH);
    Serial.println(" Device Off! ");
  }

  Serial.println();
}

void connectToMQTT()
{
  while (!mqttClient.connected())
  {
    Serial.print("Attempting MQTT connection...");

    // Create a random Client ID
    String clientId = "ESP8266Client-" + String(random(0xffff), HEX);

    // Attempt to connect
    // if your MQTT broker has ClientID, Username and Password then change following line to // if (mqttClient.connect(clientId,userName,passWord))
    if (mqttClient.connect(clientId.c_str()))
    {
      Serial.println("Connected.!");

      // Subscribe to a topic
      mqttClient.subscribe(mqttTopic);
    }
    else
    {
      Serial.print("failed, rc=");
      Serial.print(mqttClient.state());

      Serial.println(" try again in 6 seconds");
      delay(6000);
    }
  }
}
