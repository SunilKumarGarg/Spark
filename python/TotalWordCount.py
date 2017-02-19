
from pyspark import SparkContext, SparkConf

sc = SparkContext()

lines = sc.textFile("/tmp/word_count.txt")
line = lines.flatMap(lambda s: s.split(" "))
line.saveAsTextFile("/tmp/word2")
count = line.count()
print(count)
