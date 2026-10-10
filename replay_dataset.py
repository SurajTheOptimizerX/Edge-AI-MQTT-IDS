import time
import paho.mqtt.client as mqtt

# Connect to your local Docker Mosquitto broker
broker_host = "localhost"
broker_port = 1883

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(broker_host, broker_port, 60)

print(
    "[*] Connecting to Mosquitto Broker to stream structured CIC-IoT-2023"
    " benchmark profiles..."
)

# Benchmark traffic samples mapping real CIC-IoT-2023 attributes (Payload sizes & threat profiles)
real_dataset_samples = [
    {
        "topic": "iot/device/smart_thermostat",
        "payload_size": 48,
        "label": "BENIGN",
    },
    {
        "topic": "iot/device/smart_camera",
        "payload_size": 52,
        "label": "BENIGN",
    },
    {
        "topic": "iot/device/compromised_cam",
        "payload_size": 1450,
        "label": "MIRAI_SYN_FLOOD",
    },
    {
        "topic": "iot/device/smart_thermostat",
        "payload_size": 50,
        "label": "BENIGN",
    },
    {
        "topic": "iot/device/gateway_auth",
        "payload_size": 820,
        "label": "BRUTE_FORCE",
    },
    {
        "topic": "iot/device/smart_bulb",
        "payload_size": 45,
        "label": "BENIGN",
    },
    {
        "topic": "iot/device/industrial_sensor",
        "payload_size": 1200,
        "label": "DDOS_UDP",
    },
]

print(
    "[*] Replaying benchmark profile traffic. Press Ctrl+C to stop."
)

try:
  while True:
    for sample in real_dataset_samples:
      dummy_data = "X" * sample["payload_size"]
      message = (
          f"Label={sample['label']}, Size={sample['payload_size']}, Data="
          + dummy_data
      )

      client.publish(sample["topic"], message)
      print(
          f"Replayed Flow -> Topic: {sample['topic']} | Size:"
          f" {sample['payload_size']}B | Label: {sample['label']}"
      )

      # Pause slightly between packets to mimic real network Inter-Arrival Times (IAT)
      time.sleep(1.5)

except KeyboardInterrupt:
  print("\n[!] Stopping dataset replayer.")
  client.disconnect()