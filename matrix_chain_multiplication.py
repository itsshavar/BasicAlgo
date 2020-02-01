
"""
Problem Statement 
=========================
Matrix chain multiplication (or Matrix Chain Ordering Problem, MCOP) is an optimization problem that can be solved using 
dynamic programming. Given a sequence of matrices, the goal is to find the most efficient way to multiply these matrices.
The problem is not actually to perform the multiplications, but merely to decide the sequence of the matrix multiplications 
involved.

There are many options because matrix multiplication is associative. In other words, no matter how the product is 
parenthesized, the result obtained will remain the same. For example, for four matrices A, B, C, and D, we would have:

((AB)C)D = (A(BC))D = (AB)(CD) = A((BC)D) = A(B(CD)).


Runtime Analysis:
=======================
Time complexity - O(N^3)

"""
from typing import List

def matrix_chain_order(matrices : List[int]) -> int :
    matrices_length = len(matrices)

    T = [[0 for _ in range(matrices_length)] for _ in range(matrices_length)]

    for gap in range(2, matrices_length):
        for index_i in range(0, matrices_length - gap):
            index_j = index_i + gap
            T[index_i][index_j] = float('inf')
            for index_k in range(index_i + 1, index_j):
                temp = T[index_i][index_k] + T[index_k][index_j] + matrices[index_i] * matrices[index_k] * matrices[index_j]
                if temp < T[index_i][index_j]:
                    T[index_i][index_j] = temp

    return T[0][-1]


def main():
    matrices = [4, 2, 3, 5, 3]
    print(matrix_chain_order(matrices))

if __name__ == "__main__":
    main()