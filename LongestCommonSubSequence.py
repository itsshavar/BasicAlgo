
"""
Problem Statement 
=========================
The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to all sequences in a set of sequences (often just two sequences). It differs from the longest common substring problem: unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences. The longest common subsequence problem is a classic computer science problem, the basis of data comparison programs such as the diff utility, and has applications in computational linguistics and bioinformatics. It is also widely used by revision control systems such as Git for reconciling multiple changes made to a revision-controlled collection of files.



Runtime Analysis:
=======================
Time complexity - O(M * N)

"""



def LongestCommonSubSequence(String1 : str,String2 : str) -> int:
    cols = len(String1)+1
    rows = len(String2)+1
    T = [[0] * cols] * rows
    for i in range(1,rows):
        for j in range(1,cols):
            if String2[i-1] == String1[j-1]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i-1][j],T[i][j-1])

    return T[rows-1][cols-1]

def main():
    sequence1 = "ABCDGHLQR"
    sequence2 = "AEDPHR"
    print(LongestCommonSubSequence(sequence1,sequence2))

if __name__ == "__main__":
    main()