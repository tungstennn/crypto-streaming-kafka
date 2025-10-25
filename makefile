# Python virtual environment path
VENV = .venv

# Start Kafka (Zookeeper + Broker + Kafdrop)
up:
	docker compose up -d

# Stop all containers
down:
	docker compose down

# Rebuild containers
rebuild:
	docker compose down
	docker compose build
	docker compose up -d

# Run the Python Producer
producer:
	$(VENV)/bin/python producer.py

# Run the Python Consumer
consumer:
	$(VENV)/bin/python consumer.py

# Run the Streamlit dashboard
dashboard:
	streamlit run dashboard.py

# Create and activate virtual environment + install dependencies
setup:
	python -m .venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

# Clean up Docker and cache files
clean:
	docker compose down -v
	rm -rf __pycache__ */__pycache__
