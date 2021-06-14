import json
from Pub.producer import Producer


class MyProducer(Producer):
    def __init__(self, props: dict):
        super(MyProducer, self).__init__(props)

    def json_serializer(self, data) -> json:
        return json.dumps(data).encode('utf-8')


producer = MyProducer({'bootstrap_servers': 'localhost:9092'})
