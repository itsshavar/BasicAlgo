
"""
Problem Statement 
=====================================================
The change-making problem addresses the question of finding the minimum number of coins (of certain denominations) that add up to a given amount of money. 
It is a special case of the integer knapsack problem, and has applications wider than just currency.
It is also the most common variation of the coin change problem, a general case of partition in which, given the available denominations of an infinite set of coins, the objective is to find out the number of possible ways of making a change for a specific amount of money, without considering the order of the coins.


Runtime Analysis:
=======================
Time complexity - O(W * total)



"""
from typing import List

def coin_change(coins: List[int],total)->int :
    cols = total + 1
    rows = len(coins)
    T = [[0 if col == 0 else float("inf") for col in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(1, cols):
            if j < coins[i]:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = min(T[i - 1][j], 1 + T[i][j - coins[i]])

    return T[rows - 1][cols - 1]

def main():
    input = [1,5,6,8]
    total = 17
    print(coin_change(input,total))
    
if __name__ == "__main__":
    main()