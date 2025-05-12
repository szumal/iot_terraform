import time
import ssl
import paho.mqtt.client as mqtt
import json
import os

THING_NAME = "gg-demo-device"
ENDPOINT = os.getenv("IOT_ENDPOINT")
PORT = 8883

CA_PATH = "../terraform/AmazonRootCA1.pem"
CERT_PATH = "../terraform/device.pem.crt"
KEY_PATH = "../terraform/private.pem.key"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    while True:
        payload = {
            "device_id": THING_NAME,
            "timestamp": time.time(),
            "temperature": 20 + (5 * time.time() % 3)
        }
        client.publish("sensor/temp", json.dumps(payload))
        print(f"Published: {payload}")
        time.sleep(5)

client = mqtt.Client()
client.tls_set(ca_certs=CA_PATH,
               certfile=CERT_PATH,
               keyfile=KEY_PATH,
               tls_version=ssl.PROTOCOL_TLSv1_2)

client.on_connect = on_connect
client.connect(ENDPOINT, PORT)
client.loop_forever()