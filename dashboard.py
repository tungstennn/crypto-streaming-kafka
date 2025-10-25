import streamlit as st
from confluent_kafka import Consumer
import json
import time
import matplotlib.pyplot as plt

# Kafka configuration
KAFKA_BROKER = "localhost:9092"
TOPIC = "crypto_prices"
GROUP_ID = "streamlit_dashboard"

# Set up Kafka consumer
conf = {
    "bootstrap.servers": KAFKA_BROKER,
    "group.id": GROUP_ID,
    "auto.offset.reset": "latest"
}
consumer = Consumer(conf)
consumer.subscribe([TOPIC])

# Streamlit layout
st.set_page_config(page_title="Live BTC/USDT Stream", layout="wide")
st.title("📈 Real-Time Bitcoin Price (BTC/USDT)")
chart_placeholder = st.empty()

prices = []
timestamps = []

# Live loop
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        st.write(f"Consumer error: {msg.error()}")
        continue

    # Parse message
    data = json.loads(msg.value().decode("utf-8"))
    price = data.get("price")
    ts = data.get("readable_time")

    if price and ts:
        prices.append(float(price))
        timestamps.append(ts)

        # Keep chart manageable (last 50 points)
        prices = prices[-50:]
        timestamps = timestamps[-50:]

        # Draw chart
        fig, ax = plt.subplots()
        ax.plot(timestamps, prices, color="orange", marker="o")
        ax.set_xlabel("Time (UTC)")
        ax.set_ylabel("Price (USDT)")
        
        ax.ticklabel_format(style='plain', axis='y')  # disables scientific notation
        ax.get_yaxis().get_major_formatter().set_scientific(False)
        ax.grid(True, linestyle='--', alpha=0.5)

        
        plt.xticks(rotation=45)
        plt.tight_layout()
        chart_placeholder.pyplot(fig)
        plt.close(fig)

    # small sleep to avoid CPU spike
    time.sleep(0.5)
