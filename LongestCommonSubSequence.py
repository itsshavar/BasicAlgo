
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