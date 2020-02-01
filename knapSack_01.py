from typing import List
from matplotlib import mathtext

"""
Problem Statement 
=========================
The most common problem being solved is the 0-1 knapsack problem, which restricts the number {\displaystyle x_{i}} x_{i} of copies of each kind of item to zero or one. Given a set of {\displaystyle n} n items numbered from 1 up to {\displaystyle n} n, each with a weight {\displaystyle w_{i}} w_{i} and a value {\displaystyle v_{i}} v_{i}, along with a maximum weight capacity {\displaystyle W} W,

maximize ${\sum _{i=1}^{n}v_{i}x_{i}} \sum _{i=1}^{n}v_{i}x_{i}$
subject to ${\sum _{i=1}^{n}w_{i}x_{i}\leq W} \sum _{i=1}^{n}w_{i}x_{i}\leq W$ and ${x_{i}\in \{0,1\}} x_{i}\in \{0,1\}$.

Runtime Analysis:
=======================
Time complexity - O(W * total items)

"""

def knapSack(weights : List[int],values : List[int], total : int) -> int :
    cols = total + 1
    rows = len(weights) + 1
    T = [[0] * cols] * rows
    for i in range(1,rows):
        for j in range(1,cols):
            if j < weights[i -1]:
                T[i][j] = T[i-1][j]   
            else:
                T[i][j] = max(values[i-1] + T[i-1][j-weights[i-1]],T[i-1][j])
    return T[rows-1][cols-1]

def main():
    total_weight = 7
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    print(knapSack(weights,values,total_weight))


if __name__ == '__main__':
    main()