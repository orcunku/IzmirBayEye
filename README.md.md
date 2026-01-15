# IzmirBayEye AI: Izmir Bay Smart Monitoring System
**An End-to-End IoT & AI Solution for Real-time Odor Prediction and Public Safety.**

BayEye AI is a "Smart City" project designed to address the chronic odor issues in Izmir Bay. Unlike simple weather apps, this system utilizes **Biochemical Data Fusion** (Chemical, Biological, and Physical parameters) to predict odor events before they occur.

---

##  System Architecture
The project is built as a **Monorepo**, separating the high-performance backend from the citizen-facing mobile interface:

* **/src**: Python Backend (FastAPI). Handles sensor ingestion, biochemical logic, and data persistence.
* **/mobile_app**: Flutter/Dart Frontend. Real-time dashboard for citizens to monitor local air quality.
* **history.json**: A local persistence layer for trend analysis and historical logging.

---

##  Scientific Methodology
The prediction engine utilizes a multi-parameter weighted algorithm focused on **Anaerobic Decomposition cycles**. 

### The Core Logic: The H2S Trigger
The primary cause of the "rotten egg" smell in Izmir is **Hydrogen Sulfide ($H_2S$)**. This gas is produced when the bay enters a state of **Hypoxia** (low oxygen). 

### Key Parameters Monitored:
| Parameter | Role in Odor Production | Data Type |
| :--- | :--- | :--- |
| **Dissolved Oxygen (DO)** | Low levels (< 3.5mg/L) trigger $H_2S$ production. | Chemical |
| **ORP (Redox)** | Negative values indicate active organic rotting in the seabed. | Chemical |
| **Ammonia ($NH_3$)** | Proxy for sewage and industrial nitrogen discharge. | Chemical |
| **Chlorophyll-a** | Measures algae density, the primary source of organic decay. | Biological |


### The Predictive Formula:
The `AnalyticsEngine` processes these parameters using a "Penalty-Based" scoring system:
$$Risk = (BioLoad \times 0.3) + (ChemStress \times 0.5) + (MeteoFactor \times 0.2)$$

---

##  Project Structure

```text
BayEye-AI/
├── mobile_app/
│   └── main.dart          # Flutter UI mockup for citizen alerts
├── src/
│   ├── data_fetcher.py    # Simulated sensor array (Chemical/Bio/Meteo)
│   ├── engine.py          # Predictive biochemical logic & risk scoring
│   ├── main.py            # FastAPI application & REST endpoints
│   └── notifications.py   # Alert severity & notification logic
├── explanation.txt        # Detailed technical & scientific reference
├── history.json           # Local database for historical trend persistence
├── requirements.txt       # Python dependency list
└── README.md              # Project documentation


Key Features:

Proactive Alerting: Automatically generates "CRITICAL" notifications when H2S risk exceeds 80%.
Data Persistence: Logs the last 100 environmental snapshots for historical trend tracking.
Citizen UI: A Flutter-based mobile mockup showing real-time Oxygen and Risk levels.
Scientific Depth: Uses Oxidation-Reduction Potential (ORP) to detect seabed decomposition.

Potential Future Map:

Integration with real-time satellite imagery for Chlorophyll mapping.

Machine Learning (LSTM) model training on historical history.json data.

Hardware prototype using ESP32 and MQ-136 Gas Sensors.

## Methodology

The model analyzes the correlation between **Eutrophication (Algae growth)** and **Thermal Inversion**. When wind speeds drop and water temperature rises, the system alerts the municipality to activate circulation pumps.
![BayEye AI Model Analysis](MockupImage.png)

SYSTEM FLOW:

[ BAY SENSORS ]  ----(Raw Data)---->  [ FastAPI BACKEND ]
      |                                      |
(O2, ORP, NH3)                        (Predictive Logic)
                                             |
[ history.json ] <---(Log Data)--- [ Analytics Engine ]
                                             |
[ MOBILE APP ] <---(JSON Alert)--- [ Notification Service ]

