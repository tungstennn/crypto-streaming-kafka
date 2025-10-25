# ⚡ Real-Time Crypto Streaming with Kafka

This project demonstrates a **real-time data streaming pipeline** using **Apache Kafka**, **Python**, and **Streamlit**.  
It streams live Bitcoin (BTC/USDT) prices from the Binance **WebSocket API**, processes them through a **Kafka producer**,  
and visualizes them on a real-time dashboard.

---

## 🧩 Architecture Overview

**Flow:**  
Binance WebSocket API → Kafka Producer → Kafka Broker (via Docker) → Kafka Consumer / Streamlit Dashboard

**Components:**
- **WebSocket API** – Streams live crypto price updates from Binance.  
- **Producer (Python)** – Connects to Binance and sends each trade message into a Kafka topic.  
- **Kafka Broker (Docker)** – Buffers, stores, and distributes the stream.  
- **Consumer (Python)** – Reads from the Kafka topic and prints/logs the stream.  
- **Kafdrop** – Web UI to inspect Kafka topics and messages.  
- **Streamlit Dashboard** – Displays live Bitcoin price updates visually.
  
---

## Key Takeaways
- Websocket API streams real time market data
- Kafka acts as a buffer + message broket for scalability and reliability
- Streamlit provides a simple live visualisation layer

This setup models a real world streaming data architecture, from ingestion to processing to visualisation

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/crypto-streaming-kafka.git
cd crypto-streaming-kafka
```

### 2. Create / activate a virtual environment and install dependencies
```bash 
python -m venv .venv
source .venv/bin/activate   # (on Mac/Linux/WSL)
# or
.venv\Scripts\activate      # (on Windows)

pip install -r requirements.txt
```

### 3. Start Kafka and Kafdrop
```bash
make up
```
This spins up Kafka, Zookeeper, and Kafdrop using Docker Compose

### 4. Run the Producer
```bash
make producer
```
`http://localhost:9000/` to access Kafdrop

Streams live BTC/USDT prices into Kafka topic crypto_prices

### 5. Run the Consumer (optional)
```bash
make consumer
```
Prints streamed messages to the terminal

### 6. Launch the Dashboard (optional)
```bash
make dashboard
```

### Other useful commands
```bash
make down               # Stop nad remove containers
make clean              # Remove cache and volumes
make deactivate         # Deactivate virtual env 
```

