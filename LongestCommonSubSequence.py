
"""
Problem Statement 
=========================
The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to all sequences in a set of sequences (often just two sequences). 
It differs from the longest common substring problem: unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences. The longest common subsequence problem is a classic computer science problem, the basis of data comparison programs such as the diff utility, and has applications in computational linguistics and bioinformatics. It is also widely used by revision control systems such as Git for reconciling multiple changes made to a revision-controlled collection of files.



Runtime Analysis:
=======================
Time complexity - O(M * N)

"""



def LongestCommonSubSequence(sequence1 : str,sequence2 : str) -> int:
    cols = len(sequence1) + 1   # Add 1 to represent 0 valued column for DP
    rows = len(sequence2) + 1   # Add 1 to represent 0 valued row for DP
    T = [[0 for _ in range(cols)] for _ in range(rows)]
    max_length = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if sequence2[i - 1] == sequence1[j - 1]:
                T[i][j] = 1 + T[i - 1][j - 1]
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])

            max_length = max(max_length, T[i][j])

    return max_length

def main():
    sequence1 = "ABCDGHLQR"
    sequence2 = "AEDPHR"
    print(LongestCommonSubSequence(sequence1,sequence2))

if __name__ == "__main__":
    main()