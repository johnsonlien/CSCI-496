from time import time
import numpy as np
from random import random
from operator import add
import matplotlib.pyplot as plt

from pyspark.sql import SparkSession


def naive_method(n):
    hit = 0

    start = time()

    for i in range(n):
        x, y = random(), random()   # Generate random number between 0 and 1
        if x**2 + y**2 < 1:
            hit += 1

    timing = np.round(time() - start, 3)
    print("iterations: {}\t\tpi= {}\t\tseconds= {}".format(n, 4.0 * hit/n, timing))
    return np.round(time() - start, 3)     # Return the time taken to 3 decimal places


def spark_method(n, exec):

    # Function to determine if a point landed inside the unit circle
    def is_point_inside_circle(p):
        x, y = random(), random()
        return 1 if x**2 + y**2 < 1 else 0

    # Start the timer
    start = time()

    # Create RDD and map function to clusters
    # Add the results together
    # Return the time taken
    count = sc.parallelize(range(0, n), exec) \
        .map(is_point_inside_circle).reduce(add)
    timing = np.round(time() - start, 3)
    print("iterations= {}\t\tpi= {}\t\tseconds= {}".format(n, (4.0 * count/n), timing))
    return timing

# Initialize Spark environment
spark = SparkSession.builder.appName('EstimatePi').getOrCreate()
sc = spark.sparkContext

# Number of iterations
N = [10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000]

# Buffers to record the time taken for naive, default, and 2 clusters, respectively
T = []
T_spark = []
T_spark_2_executors = []

# Run naive and default Spark version
print("\n===== Naive Method =====")
for n in N:
    T.append(naive_method(n))               # Naive method

print("\n===== Spark Method 4 clusters =====")
for n in N:
    T_spark.append(spark_method(n, 4))     # Default Spark method (4 clusters)

# Stop the Spark session
spark.stop()

# Since we cannot have 2 different sparks running at the same time, we close the previous
# one and start a new one and initialize how many clusters we want to use
# Run Spark version with 2 clusters
spark = SparkSession.builder.appName('EstimatePi').getOrCreate()
sc = spark.sparkContext
print("\n===== Spark Method 2 clusters =====")
for n in N:
    T_spark_2_executors.append(spark_method(n, 2))

spark.stop()

plt.plot(N, T, label="naive")
plt.plot(N, T_spark, label="spark - 4 exec")
plt.plot(N, T_spark_2_executors, label="spark - 2 exec")

plt.xscale("log")
plt.xlabel("Total number of points.")
plt.ylabel("Time to estimate pi (sec.)")
plt.legend()
plt.show()