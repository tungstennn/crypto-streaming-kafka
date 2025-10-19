from confluent_kafka import Consumer, KafkaException, KafkaError
import json

BROKER = "localhost:9092"
TOPIC = "crypto_prices"


# Configure the consumer
conf = {
    'bootstrap.servers': BROKER,
    'group.id': 'crypto-consumer-group',
    'auto.offset.reset': 'latest'  # start reading from the newest messages
}

consumer = Consumer(conf)
consumer.subscribe([TOPIC])

print(f"✅ Listening for messages on topic: {TOPIC}\n")

try:
    while True:
        msg = consumer.poll(1.0)  # wait up to 1 second for a message
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                raise KafkaException(msg.error())
        
        # Decode the message
        data = json.loads(msg.value().decode('utf-8'))
        print(f"Symbol: {data['symbol']}, Price: {data['price']}, Event Time: {data['event_time']}")

except KeyboardInterrupt:
    print("\n🛑 Stopped by user.")
finally:
    consumer.close()
