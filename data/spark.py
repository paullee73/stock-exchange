from pyspark import SparkContext
from itertools import combinations
import MySQLdb

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)
user_item = data.map(lambda line: line.split(","))
user_itemList = user_item.groupByKey()
userComb = user_itemList.map(
    lambda x: (x[0], combinations(x[1], 2)))
userComb = userComb.flatMapValues(lambda x: x)
itemComb = userComb.map(lambda x: (x[1], x[0]))
itemComb = itemComb.groupByKey()
itemCombinations_count = itemComb.map(lambda x: (x[0], len(x[1])))

# itemCombinations_count_filtered = itemCombinations_count.filter(
#     lambda x: x[1] >= 3)

output = itemCombinations_count.collect()
for item_pair, count in output:
    print('{} {}'.format(item_pair, count))

sc.stop()

db = MySQLdb.connect(host="db", port=3306, user="www",
                     passwd="$3cureUS", db="cs4501")
cursor = db.cursor()
cursor.execute("TRUNCATE TABLE stockapp_recommendations;")

db.commit()

pair_dict = {}
for item_pair, count in output:
    if not item_pair[0] in pair_dict:
        pair_dict[item_pair[0]] = item_pair[1] + ','
    else:
        pair_dict[item_pair[0]] += item_pair[1] + ','
    if not item_pair[1] in pair_dict:
        pair_dict[item_pair[1]] = item_pair[0] + ','
    else:
        pair_dict[item_pair[1]] += item_pair[0] + ','

for key, value in pair_dict.items():
    cursor.execute(
        "INSERT INTO stockapp_recommendations (item, recommended_items) VALUES (\'{}\',\'{}\')".format(str(key), str(value)))

db.commit()
cursor.execute("""SELECT * FROM stockapp_recommendations""")
print(cursor.fetchall())
cursor.close()
db.close()
