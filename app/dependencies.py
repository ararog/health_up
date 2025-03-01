import json
from decouple import config
from kafka import KafkaProducer

def get_kafka_producer():
  return KafkaProducer(bootstrap_servers=config("KAFKA_BROKER"), 
                       value_serializer=lambda m: json.dumps(m).encode('ascii'))