from time import time
import numpy as np
from random import random
from operator import add
import matplotlib.pyplot as plt
import math

from pyspark.sql import SparkSession


def naive_method(n):
    hit = 0

    start = time()

    for i in range(n):
        x, y = random(), random()   # Generate random number between 0 and 1
        if x**2 + y**2 < 1:
            hit += 1

    pi_estimate = 4.0 * hit / n
    timing = np.round(time() - start, 3)
    print("iterations: {}\t\tpi= {}\t\tseconds= {}".format(n, pi_estimate, timing))
    # return timing     # Return the time taken to 3 decimal places
    return pi_estimate, timing
# End naive_method()

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
    pi_estimate = 4.0 * count / n
    timing = np.round(time() - start, 3)
    print("iterations= {}\t\tpi= {}\t\tseconds= {}".format(n, pi_estimate, timing))
    # return timing
    return pi_estimate, timing
# End spark_method()

# Initialize Spark environment
spark = SparkSession.builder.appName('EstimatePi').getOrCreate()
sc = spark.sparkContext

# Number of iterations
N = [10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000]

# Buffers to record the time taken for naive, default, and 2 clusters, respectively
T = []
T_spark_2_executors = []
T_spark_4_executors = []

# Buffers to record the value of pi for naive, 2 executers, and 4 executors
P = []
P_spark_2_executors = []
P_spark_4_executors = []

# Run naive and default Spark version
print("\n===== Naive Method =====")
for n in N:
    pi, t = naive_method(n)
    P.append(pi)
    T.append(t)               # Naive method

print("\n===== Spark Method 4 clusters =====")
for n in N:
    pi, t = spark_method(n, 4)
    P_spark_4_executors.append(pi)
    T_spark_4_executors.append(t)     # Default Spark method (4 clusters)

# Stop the Spark session
spark.stop()

# Since we cannot have 2 different sparks running at the same time, we close the previous
# one and start a new one and initialize how many clusters we want to use
# Run Spark version with 2 clusters
spark = SparkSession.builder.appName('EstimatePi').getOrCreate()
sc = spark.sparkContext
print("\n===== Spark Method 2 clusters =====")
for n in N:
    pi, t = spark_method(n, 2)
    P_spark_2_executors.append(pi)
    T_spark_2_executors.append(t)

spark.stop()

# Plot time taken for each iteration
plt.figure(1)
plt.plot(N, T, label="naive")
plt.plot(N, T_spark_2_executors, label="spark - 2 exec")
plt.plot(N, T_spark_4_executors, label="spark - 4 exec")

plt.xscale("log")
plt.xlabel("Total number of points.")
plt.ylabel("Time to estimate pi (sec.)")
plt.legend()
plt.show()

# Plot convergence of pi estimate
plt.figure(2)
plt.plot(N, P, label="naive")
plt.plot(N, P_spark_2_executors, label="spark - 2 exec")
plt.plot(N, P_spark_4_executors, label="spark - 4 exec")
plt.hlines(y=math.pi, xmin=0, xmax=100000000, colors='k', linestyles='dashed', label="pi")

plt.xscale("log")
plt.xlabel("Total Number of Iterations")
plt.ylabel("Pi Estimate")
plt.legend()
plt.show()
