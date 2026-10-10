import time
import paho.mqtt.client as mqtt

# Define broker details
BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor/telemetry"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with result code {rc}")
    # Subscribe to the topic once connected
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"📥 Received Message -> Topic: {msg.topic} | Payload: {msg.payload.decode()}")

# Initialize MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to our Docker broker
client.connect(BROKER, PORT, 60)

# Start a background network loop
client.loop_start()

# Simulate an IoT sensor sending data every 2 seconds
try:
    count = 1
    while True:
        payload = f"Sensor_Node_1: Temperature=24.{count}C, Status=Normal"
        print(f"📤 Publishing -> {payload}")
        client.publish(TOPIC, payload)
        count += 1
        time.sleep(2)
except KeyboardInterrupt:
    print("Stopping client...")
    client.loop_stop()
    client.disconnect()