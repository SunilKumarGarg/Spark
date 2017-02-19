from pyspark import SparkContext, SparkConf
import random

sc = SparkContext()


def sample(p):
    x, y = random.random(), random.random()
    return 1 if x*x + y*y < 1 else 0

count = sc.parallelize(range(0, 1000)).map(sample).reduce(lambda a, b: a + b)
print "Pi is roughly %f" % (4.0 * count / 1000)