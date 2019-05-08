from kafka import KafkaConsumer
import json
import time
import os

consumer = None
while(True):
    try:
        consumer = KafkaConsumer(
            'map-reduce-topic', group_id='listing', bootstrap_servers=['kafka:9092'])
        break
    except:
        time.sleep(3)
        continue
for message in consumer:
    new_listing = json.loads((message.value).decode('utf-8'))
    print(new_listing)
    with open("/tmp/data/access.log", 'a') as file:
        file.write(str(new_listing['userID']) + "," +
                   str(new_listing['ticker_symbol']) + '\n')
