#!/usr/bin/env bash
docker exec -it spark-master bash -c "apt-get update && apt-get install python3-dev default-libmysqlclient-dev -y && apt-get install python-pip -y && pip install mysqlclient && apt-get install python-mysqldb"
docker exec -it spark-worker bash -c "apt-get update && apt-get install python3-dev default-libmysqlclient-dev -y && apt-get install python-pip -y && pip install mysqlclient && apt-get install python-mysqldb"

while true;
do
	docker exec -it spark-master bin/spark-submit --master spark://spark-master:7077 --total-executor-cores 2 --executor-memory 512m /tmp/data/spark.py
	sleep 120
done
