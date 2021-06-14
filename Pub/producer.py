import json
from kafka import KafkaProducer
from abc import ABC, abstractmethod


class Producer(ABC):
    def __init__(self, props: dict):
        self.producer = KafkaProducer(
            bootstrap_servers=[props['bootstrap_servers']],
            value_serializer=self.json_serializer)

    def send(self, topic_name: str, key: str, message: dict):
        self.producer.send(topic=topic_name, key=key, value=message)

    @abstractmethod
    def json_serializer(self, data) -> json:
        pass
