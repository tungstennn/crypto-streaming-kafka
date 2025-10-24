# crypto-streaming-kafka

This project demonstrates a real-time cryptocurrency data streaming pipeline using Apache Kafka, Python, and Docker. 


It continuously streams live trade data for Bitcoin (BTC/USDT) from the Binance WebSocket API and publishes each message to a Kafka topic named `crypto_prices`. The system is containerized with Docker Compose, which runs Kafka, Zookeeper, and Kafdrop (a lightweight web UI for monitoring Kafka topics and message flow). A Python producer script ingests the data in real time, appending both a raw event timestamp and a human-readable UTC timestamp for clarity and traceability. A Python consumer script can then subscribe to the same topic and display messages as they arrive, enabling near real-time analytics or downstream integration. Overall, this project provides a practical introduction to event-driven architectures, message queuing, and real-time data pipelines, ideal for learning how to build scalable streaming systems for data engineering or analytics use cases.


### Components
- **Docker** — runs Kafka, Zookeeper, and Kafdrop.
- **Kafka Broker** — message queue where all live crypto trades are published.
- **Producer (Python)** — connects to Binance WebSocket and streams trade data into Kafka.
- **Consumer (Python)** — subscribes to the Kafka topic and prints or processes messages.
- **Kafdrop** — web-based Kafka UI for inspecting topics and messages.
