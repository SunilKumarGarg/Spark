
from pyspark import SparkContext, SparkConf

sc = SparkContext()

lines = sc.textFile("/tmp/word_count.txt")
line = lines.flatMap(lambda s: s.split(" ")).map(lambda s: (s,1)).reduceByKey(lambda a, b: a+b)

print(line.collect())
line.saveAsTextFile("/tmp/word")