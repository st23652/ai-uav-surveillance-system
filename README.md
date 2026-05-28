# AI-Powered Autonomous Surveillance & Emergency Response Drone System

Real-time UAV surveillance framework integrating artificial intelligence, drone telemetry, embedded sensing, and operator monitoring into a unified aerial safety research platform.

---

# Overview

The **AI-Powered Autonomous Surveillance & Emergency Response Drone System** is a research-oriented UAV platform designed to investigate the integration of computer vision, embedded systems, and autonomous aerial monitoring technologies for rapid situational awareness.

The system combines:

* UAV-based live video streaming
* AI-powered human activity analysis
* Embedded environmental sensing
* Real-time telemetry monitoring
* Secure operator authentication
* Centralized monitoring dashboard

The platform was developed as an academic research prototype to explore how intelligent aerial systems can assist human operators during emergency monitoring and surveillance scenarios.

---

# Key Features

## UAV Integration

* DJI Tello drone communication
* Real-time telemetry retrieval
* Wireless UAV control
* Live aerial video streaming

## AI Surveillance

* Real-time human detection
* Pose estimation pipeline
* Behaviour analysis
* Suspicious activity monitoring

## Embedded Systems

* ESP32-based sensing module
* Multi-directional obstacle awareness
* Time-of-Flight distance sensing
* WiFi sensor communication

## Monitoring Dashboard

* Live UAV video feed
* Mission control interface
* Sensor monitoring panels
* AI analytics visualization
* System health monitoring

## Security

* OTP-based operator authentication
* Session validation
* Access-controlled monitoring system

---

# System Architecture

The platform consists of four major subsystems working together in a modular architecture.

```text
                    ┌──────────────────────┐
                    │   DJI TELLO DRONE   │
                    └──────────┬──────────┘
                               │
                     Live Video Stream
                               │
                               ▼
                    ┌──────────────────────┐
                    │   AI DETECTION       │
                    │      ENGINE          │
                    └──────────┬──────────┘
                               │
               Detection Results & Analytics
                               │
                               ▼
                    ┌──────────────────────┐
                    │   FASTAPI BACKEND    │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┴────────────────────┐
          │                                         │
          ▼                                         ▼
┌──────────────────────┐              ┌──────────────────────┐
│  WEB DASHBOARD       │              │   ESP32 SENSOR       │
│  Monitoring System   │              │   SUBSYSTEM          │
└──────────────────────┘              └──────────────────────┘
```

---

# Technologies Used

## Programming Languages

* Python
* PHP
* JavaScript
* HTML/CSS
* C++

## AI & Computer Vision

* YOLOv8
* PyTorch
* OpenCV
* NumPy

## Backend

* FastAPI
* Uvicorn

## Drone Communication

* DJITelloPy

## Embedded Systems

* ESP32-C3 Super Mini
* VL53L0X ToF Sensors
* TCA9548A I2C Multiplexer

---

# Repository Structure

```text
ai-uav-surveillance-system/
│
├── README.md
├── requirements.txt
├── assets/
│   ├── architecture/
│   ├── screenshots/
│   └── demo/
│
├── src/
│   │
│   ├── backend/
│   │   ├── main.py
│   │   ├── api.py
│   │   ├── drone_controller.py
│   │   ├── video_stream.py
│   │   ├── ai_engine.py
│   │   └── auth.py
│   │
│   ├── frontend/
│   │   ├── dashboard.php
│   │   ├── mission.php
│   │   ├── intelligence.php
│   │   ├── embedded.php
│   │   ├── analytics.php
│   │   └── system_health.php
│   │
│   └── embedded/
│       ├── esp32_sensor_node.ino
│       └── sensor_config.h
│
└── docs/
    ├── hardware_setup.md
    ├── api_documentation.md
    └── research_notes.md
```

---

# Core Modules

## 1. Drone Control Module

The drone control subsystem manages communication with the DJI Tello UAV using Python-based SDK integration.

### Responsibilities

* Drone connection
* Flight commands
* Telemetry retrieval
* Video stream activation

### Example Functions

```python
# Connect to the drone
tello.connect()

# Start video streaming
tello.streamon()

# Retrieve battery percentage
battery = tello.get_battery()
```

---

## 2. AI Detection Engine

The AI subsystem processes live UAV video frames to detect human presence and analyse activity patterns.

### Features

* Human detection
* Pose estimation
* Real-time inference
* Detection overlays

### Example Workflow

```python
# Load YOLOv8 model
model = YOLO("yolov8n-pose.pt")

# Run inference on frame
results = model(frame)

# Process detection results
for result in results:
    print(result)
```

---

## 3. Embedded Sensor System

The embedded sensing module provides environmental awareness using distance sensors connected to an ESP32 microcontroller.

### Hardware Components

* ESP32-C3 Super Mini
* TCA9548A Multiplexer
* VL53L0X ToF Sensors

### Example Sensor Logic

```cpp
// Read distance from sensor
distance = sensor.readRangeSingleMillimeters();

// Send sensor value
Serial.println(distance);
```

---

## 4. Monitoring Dashboard

The web dashboard provides centralized monitoring and interaction with the UAV system.

### Dashboard Modules

* Mission Control
* AI Intelligence
* Embedded Monitoring
* Analytics
* System Health
* Records

### Example API Retrieval

```php
// Fetch telemetry data
$response = file_get_contents($api_url);

// Decode JSON response
$data = json_decode($response, true);
```

---

# Installation & Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/ai-uav-surveillance-system.git

cd ai-uav-surveillance-system
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend Server

```bash
uvicorn src.backend.main:app --reload
```

Backend server:

```text
http://127.0.0.1:8000
```

---

## Start Dashboard

```bash
php -S localhost:8080
```

Dashboard:

```text
http://localhost:8080
```

---

# Hardware Setup

## Components Required

| Component           | Purpose             |
| ------------------- | ------------------- |
| DJI Tello Drone     | UAV platform        |
| ESP32-C3 Super Mini | Embedded controller |
| VL53L0X Sensors     | Distance sensing    |
| TCA9548A            | I2C multiplexing    |
| Breadboard & Wiring | Sensor connections  |

---

# Research Objectives

The project investigates:

* Real-time aerial violence detection
* UAV-assisted situational awareness
* Integration of AI with aerial robotics
* Embedded environmental monitoring
* Real-time operator support systems

---

# Ethical Considerations

This project was developed solely for academic research purposes.

The system:

* does not perform facial recognition
* does not identify individuals
* uses staged experimental scenarios
* follows ethical research practices

---

# Future Improvements

Potential future development includes:

* Autonomous UAV navigation
* Multi-drone coordination
* Edge AI optimization
* Advanced behaviour recognition
* Thermal camera integration
* Cloud analytics support

---

# Screenshots

## Suggested Images To Add

### Dashboard

```text
assets/screenshots/dashboard_main.png
```

### AI Detection

```text
assets/screenshots/ai_detection.png
```

### Drone Flight

```text
assets/screenshots/drone_operation.png
```

### Embedded Sensors

```text
assets/screenshots/sensor_module.png
```

---

# Suggested GitHub Topics

Add these GitHub repository topics:

```text
uav
drone
computer-vision
yolov8
ai-surveillance
fastapi
opencv
embedded-systems
esp32
robotics
iot
research-project
```

---

# Suggested Portfolio Description

> Research-focused UAV surveillance platform integrating AI-based violence detection, embedded sensing, drone telemetry, and real-time monitoring into a unified aerial emergency response system.

---

# License

This project is released for academic and research purposes only.

---

# Author

**Sneha Tandon**

