from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
import time 

es = Elasticsearch(['es'])
consumer = None 
while(True):
	try:
		consumer = KafkaConsumer('new-listings-topic', group_id='listing', bootstrap_servers=['kafka:9092'])
		break
	except:
		time.sleep(3)
		continue
for message in consumer:
		new_listing = json.loads((message.value).decode('utf-8'))
		es.index(index='listing_indexer', doc_type='listing', id=new_listing['id'], body=new_listing)
		es.indices.refresh(index='listing_indexer')