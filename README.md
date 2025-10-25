# ⚡ Real-Time Crypto Streaming with Kafka

This project demonstrates a **real-time data streaming pipeline** using **Apache Kafka**, **Python**, and **Streamlit**.  
It streams live Bitcoin (BTC/USDT) prices from the Binance **WebSocket API**, processes them through a **Kafka producer**, and visualizes them on a real-time dashboard.

---

## Architecture Overview

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
Through this project, I deepened my understanding of:
- How WebSocket APIs enable continuous, real-time data streaming.
- The difference between WebSockets and REST APIs — WebSockets maintain an open connection for instant updates.
- Why introducing Kafka as a middle layer (instead of connecting consumers directly to WebSockets) improves scalability, reliability, fault tolerance, and data replayability.
- How Streamlit can be used to visualize real-time data in a lightweight, responsive dashboard.

Overall, this project helped me connect the dots between data ingestion, stream processing, and real-time analytics.

---

## Future Improvements

There are several directions to extend this project for more practical, production-like use:
1. Integrate a database sink (PostgreSQL, MongoDB, or S3)
    - Store historical trade data from Kafka for long-term analysis
    - Enables querying and trend analytics beyond the short-lived Kafka retention window

2. Batch or micro-batch ingestion pipeline

    - Use a consumer script to periodically write Kafka data to a database
    - Adds durability and decouples live streaming from storage

3. Enhanced dashboard analytics
    - Add charts for hourly averages, volatility tracking, or percentage changes
    - Use a cached data layer or in-memory aggregation for smoother updates

4. Containerize the full workflow (producer + dashboard)
    - Ensures full portability across machines using Docker Compose or Kubernetes

5. Implement alerting
    - Stream real-time price thresholds to trigger alerts (email, Slack, etc)

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
make down               # Stop and remove containers
make clean              # Remove cache and volumes
make deactivate         # Deactivate virtual env 
```

