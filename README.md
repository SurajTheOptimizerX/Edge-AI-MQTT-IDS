<div align="center">

  <h1>⚡ Edge-AI IoT-IDS</h1>
  <h3>Edge-Optimized AI-Driven Intrusion Detection System for MQTT-Enabled IoT Networks</h3>

  <p>
    <em>“Shielding the connected world with sub-millisecond edge intelligence and automated threat mitigation.”</em>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python" />
    <img src="https://img.shields.io/badge/ONNX-Runtime-black?style=for-the-badge&logo=onnx" alt="ONNX" />
    <img src="https://img.shields.io/badge/Eclipse-Mosquitto-green?style=for-the-badge&logo=eclipse" alt="MQTT" />
    <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit" alt="Streamlit" />
    <img src="https://img.shields.io/badge/CIC--IoT--2023-33%20Vectors-purple?style=for-the-badge&logo=security" alt="CIC-IoT-2023" />
  </p>

  <p>
    <strong>Sub-5ms ONNX CPU Inference</strong> &nbsp;•&nbsp;
    <strong>33 CIC-IoT-2023 Attack Vectors</strong> &nbsp;•&nbsp;
    <strong>Automated Broker ACL Isolation</strong> &nbsp;•&nbsp;
    <strong>Real-Time SIEM SOC Dashboard</strong>
  </p>

  <p>
    📍 <em>Engineered for IIIT Bhopal MCA Master's Research Project (Course: MCA-3005 Project Design)</em>
  </p>

</div>

---

## 📑 Table of Contents
1. [Project Title & Team Details](#-project-title--team-details)
2. [Live Simulation & Demo](#-live-simulation--demo)
3. [Problem Statement & Research Context](#-problem-statement--research-context)
4. [Solution & System Architecture](#-solution--system-architecture)
5. [Technology Stack](#-technology-stack)
6. [Key Features & Highlights](#-key-features--highlights)
7. [Installation & Setup Guide (Step-by-Step)](#-installation--setup-guide-step-by-step)
8. [Execution Instructions](#-execution-instructions)
9. [Future Scope & Federated Learning](#-future-scope--federated-learning)

---

## 👥 Project Title & Team Details

- **Project Title:** Edge-Optimized AI-Driven Intrusion Detection System (IoT-IDS) for MQTT-Enabled IoT Networks[cite: 3]
- **Institution:** Indian Institute of Information Technology, Bhopal (IIIT Bhopal) — Department of Information Technology
- **Degree Program:** Master of Computer Applications (MCA) — Second Year, Third Semester (Course: MCA-3005 Project Design)

### 👥 Team Members

| Role | Member Name | Roll Number / ID | Email Address | GitHub Profile |
| :--- | :--- | :--- | :--- | :--- |
| **👑 Team Lead / ML Architect** | **Ritik Agarwal** | `25P03F0050`[cite: 4] | agarwalritik895@gmail.com | [@RIITKAGARWAL](https://github.com/RIITKAGARWAL) |
| **🐳 Infrastructure Developer** | **Suraj Sahu** | `25P03F0047`[cite: 4] | surajsahusrjs@gmail.com | [Insert GitHub] |
| **⚡ Inference Engine Developer** | **Rahul Verma** | `25P03F0049`[cite: 4] | rahulverma945717@gmail.com | [Insert GitHub] |
| **🛡️ UI & Mitigation Lead** | **Aarushi Khandelwal** | `25P03F0005`[cite: 4] | aarushi11khandelwal@gmail.com | [Insert GitHub] |

---

## 🌐 Live Simulation & Demo

- **Repository:** https://github.com/RIITKAGARWAL/Edge-AI-IoT-IDS
- **Status:** Active Development / Design Phase (Phase 1 Completed)[cite: 8]

---

## 🎯 Problem Statement & Research Context

### Real-World Context
Modern smart infrastructures—including IP cameras, smart city sensors, industrial telemetry, and medical monitors—rely heavily on the lightweight publish-subscribe **MQTT (Message Queuing Telemetry Transport)** protocol[cite: 3]. However, these systems face critical cyber threats such as Distributed Denial of Service (DDoS), volumetric flooding, brute-force exploits, packet spoofing, and automated Mirai botnet incursions[cite: 3].

### Research Gaps Addressed
1. **The Perimeter Blindspot:** Traditional enterprise firewalls inspect North-South (WAN-to-LAN) traffic, leaving them blind to internal **East-West lateral movement** when an infected internal device attacks local brokers and peer endpoints[cite: 3].
2. **Resource Constraints:** IoT endpoints operate on resource-constrained microcontrollers ($\le 64$ KB to a few megabytes of RAM), making heavy host-level EDR software impossible[cite: 3].
3. **Protocol Incompatibility:** Legacy signature engines (Snort/Suricata) are optimized for HTTP/HTTPS web traffic and fail to parse compact binary or JSON payloads native to MQTT[cite: 3].

---

## 🚀 Solution & System Architecture

Edge-AI IoT-IDS provides an edge-native, zero-budget security architecture[cite: 3]:
- **Message Broker Integration:** Deployed on an Eclipse Mosquitto MQTT broker (Port 1883) acting as a transparent security bump-in-the-wire[cite: 4].
- **Behavioral Feature Extraction:** Intercepts streaming packets to compute **Payload Size (Bytes)** and **Inter-Arrival Time (IAT)** deltas[cite: 4].
- **ONNX Runtime Acceleration:** Compiles tree-based ensemble models into an optimized `.onnx` graph format, achieving deterministic **$\le 1.45\text{ ms}$ CPU per-packet inference**[cite: 4].
- **Automated Mitigation:** Instantly revokes client publishing rights at the broker Access Control List (ACL) level when high-confidence anomalies ($>99.5\%$) are detected[cite: 4].

---

## 🛠️ Technology Stack

- **Core Language:** Python 3.10+[cite: 9]
- **Message Broker:** Eclipse Mosquitto (MQTT v3.1.1 / v5.0 compliant)[cite: 9]
- **AI / ML Frameworks:** Scikit-Learn, XGBoost, ONNX Runtime[cite: 9]
- **Packet Inspection:** Scapy, Paho-MQTT[cite: 9]
- **Containerization:** Docker & Docker-Compose[cite: 9]
- **Web Dashboard:** Streamlit[cite: 9]

---

## 🌟 Key Features & Highlights

1. **33 CIC-IoT-2023 Vector Coverage:** Explicitly handles all 33 variants across 7 major attack families (DDoS, DoS, Mirai Botnet, Reconnaissance, Brute Force, Web-Based Attacks, and Spoofing/MITM)[cite: 4].
2. **Sub-5ms Inference Latency:** Eliminates Python interpreter bloat via C++ ONNX runtime graph execution[cite: 4].
3. **Interactive Sidebar Control Panel:** Complete manual test bench categorized into 7 expandable dropdowns for isolated attack simulation.
4. **Enterprise SIEM Feed:** Renders multi-line structured forensic incident reports (`st.code`) with exact payload metadata, confidence metrics, and rationale trees.

---

## 💻 Installation & Setup Guide (Step-by-Step)

### Prerequisites
- **Python 3.10 or higher** installed on your system[cite: 9].
- **Docker & Docker-Compose** (for running the Mosquitto MQTT broker container)[cite: 9].
- **Git** for cloning the repository.

### Step 1: Clone the Repository
```bash
git clone https://github.com/RIITKAGARWAL/Edge-AI-IoT-IDS.git
cd Edge-AI-IoT-IDS
```

### Step 2: Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install streamlit pandas numpy onnxruntime paho-mqtt scikit-learn xgboost
```

### Step 4: Start the Mosquitto MQTT Broker via Docker
Ensure Docker is running on your machine, then spin up the broker container:
```bash
docker run -it -p 1883:1883 -p 9001:9001 eclipse-mosquitto
```

---

## ▶️ Execution Instructions

To run the complete real-time intrusion detection pipeline, open **two separate terminal windows** (both activated within your virtual environment):

### Terminal 1: Start the Backend AI Security Gateway
```bash
python feature_extractor.py
```

### Terminal 2: Launch the Streamlit SOC Dashboard
```bash
streamlit run app.py
```

---

## 🔮 Future Scope & Federated Learning

- **Federated Learning (FL) Integration:** Future iterations will explore distributed collaborative training across multiple isolated edge subnets. Rather than centralizing raw network telemetry, distributed gateways will collaboratively update global XGBoost/ONNX model weights by exchanging only gradient parameters, preserving absolute data privacy while mitigating zero-day lateral movements[cite: 9].
- **Hardware In-the-Loop Validation:** Deployment onto physical low-cost single-board computers (e.g., Raspberry Pi 4, NVIDIA Jetson Nano) to profile thermal dissipation and energy draw under active volumetric floods[cite: 9].

---

<div align="center">
  <p>Built with ⚡ and Rigorous Engineering by <strong>Team IoT-IDS (IIIT Bhopal)</strong>[cite: 3, 4]</p>
</div>
