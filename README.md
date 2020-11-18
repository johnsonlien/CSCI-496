# CSCI-496 Final Project Due 11/18/2020
Final submission. Topic: Community Detection with PySpark API 

# Problem:
Can I predict/find influential users within a community? 

# What is the drive behind this?
Business promotion. By identifying influential users, or being able to predict who is influential, you can target advertisment around those users and promote a business or its product. Can incentivize users to go to some store and gather people with common interests.

# Solution: Apache Spark's PySpark
## What is PySpark?
PySpark is one of APIs for Apache Spark and supports the usage of R, Java, Scala, and Python. PySpark is the Python API for Apache Spark. Pyspark API runs on the Hadoop File System (HDFS) and allows developers to compute programs in clusters. 
![Apache Spark Overview](https://d1.awsstatic.com/Data%20Lake/what-is-apache-spark.b3a3099296936df595d9a7d3610f1a77ff0749df.PNG)

## How does it work?
Spark programs consist of a driver node (a main function) that initiates the environment and worker nodes to conduct the computations.

![PySpark Cluster](https://spark.apache.org/docs/latest/img/cluster-overview.png)

A data structure known as Resilient Distributed Dataset (RDD) is used to distribute the data to those worker nodes. RDDs are generally in the form of dictionaries or arrays. 
A [list of packages](https://spark.apache.org/docs/latest/api/python/index.html) are included with PySpark but we will be using a 3rd-party package to solve our community detection problem called GraphFrames. 

## GraphFrames
GraphFrames is a 3rd-party software built on PySpark that specializes in graph and graph functions. PySpark already has a built-in graph computation but GraphX is only for Scala. GraphFrames uses a data structure similar to RDDs known as DataFrames.

## Label Propagation Algorithm
GraphFrames has a built-in community detection algorithm that we can use. The results should be similar to the following image.
![LPA](https://d3i71xaburhd42.cloudfront.net/693280813d1e39120067e40338dccad9d2e857ea/5-Figure4-1.png)

# Apache Spark Official Website
Apache Spark's website to learn more is located [here](https://spark.apache.org/docs/3.0.1/) and contains the overview of the API. 

