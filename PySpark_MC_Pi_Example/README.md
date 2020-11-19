# Monte Carlo Estimation of Pi
This folder demonstrates an example of PI estimation using PySpark.
## General Idea of Monte Carlo Simulation
The idea is simple. Generate some number of points with coordinates (x, y) where 0 <= x <= 1 and 0 <= y <= 1. 
Count the number of points that lie inside the unit circle and the total number of points generated. 
Divide the number of points inside the circle by the total number of points and multiply by 4 (because the points are only in the first quadrant) and that'll give you an estimation of pi.
![](https://nclab.com/wp-content/media/2017/08/pi1.gif)

## PySpark MC Estimation of Pi
The program will estimate pi using different numbers of iterations N = [10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 50000000, 100000000]. For each iteration, n, we 
store the range from 0 to n into an RDD using Spark's parrellize() function. This will split up the work into different executors and speed up the computation time. 
