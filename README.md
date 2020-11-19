# CSCI-596 Final Project Due 11/18/2020
Final submission. Topic: Community Detection with PySpark API 

# The Problem
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
[GraphFrames](https://graphframes.github.io/graphframes/docs/_site/index.html) is a 3rd-party package built for PySpark that specializes in graph computations. PySpark already has a built-in graph computation but GraphX is only for Scala. GraphFrames uses a data structure similar to RDDs known as DataFrames. 

# GraphFrame's Community Detection Algorithm
GraphFrames has a built-in community detection algorithm that we can use called Label Propagation Algorithm (LPA). The results should be similar to the following image.

![LPA](https://github.com/johnsonlien/CSCI-596/blob/main/lpa.png?raw=true)

# How do you determine an inflential user?
There are many different factors to determine a user's influence so there is no clear cut answer to this. One idea is the PageRank algorithm where it determines a nodes "importance" based on the number of incoming edges. Depending on the social platform used, there would be different factors. 

# Apache Spark Official Website
Apache Spark's website to learn more is located [here](https://spark.apache.org/docs/3.0.1/) and contains the overview of the API. 

Note: Because this is an unpublished research project, there is no actual code to show regarding this community detection. There is only a broad overview of the plan.

If you have any questions regarding PySpark, I will try my best to answer.

my email: jtlien@usc.edu

# Quick PySpark Demo for Monte Carlo Simulation of Pi
Just for a quick demonstration of PySpark, I have included a python file that estimates Pi using Monte Carlo simulation. 
![](https://github.com/johnsonlien/CSCI-596/blob/main/pyspark_mc_pi.PNG?raw=true)
![](https://github.com/johnsonlien/CSCI-596/blob/main/pyspark_pi_convergence.png?raw=true)
