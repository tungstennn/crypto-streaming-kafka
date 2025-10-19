from confluent_kafka import Producer
import json, asyncio, websockets
from datetime import datetime

BROKER = "localhost:9092"
TOPIC = "crypto_prices"


readable_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

p = Producer({'bootstrap.servers': BROKER})

async def produce():
    url = "wss://stream.binance.com:9443/ws/btcusdt@trade"
    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            price = float(data["p"])
            event_time = data["E"]

            payload = json.dumps({
                "symbol": "BTCUSDT",
                "price": price,
                "event_time": event_time,
                "readable_time" : datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            })

            p.produce(TOPIC, value=payload)
            p.flush()

asyncio.run(produce())
