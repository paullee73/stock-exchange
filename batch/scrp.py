from kafka import KafkaConsumer
from elasticsearch import Elasticsearch

while(True):
	consumer = KafkaConsumer('new-listings-topic'), group_id='listing'