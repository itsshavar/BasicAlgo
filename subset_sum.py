from typing import List
def subset_sum(input: List[int],total : int) -> int:
    """
    cols = total + 1
    rows = len(input) + 1
    T = [[False] * cols] * rows
    for i in range(rows):
        T[i][0] = True
    print(T)
    for i in range(1,rows):
        for j in range(1,cols):
            if j >= input[i-1]:
                T[i][j] = T[i-1][j] or T[i-1][j-input[i-1]]
            else:
               T[i][j] = T[i-1][j]
        
    return T[rows-1][cols-1]
    """
    
    """
    cols = total + 1         # Plus 1 for 0 valued col.
    rows = len(input) + 1     # Plus 1 for 0 valued row.
    T = [[False for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        T[row][0] = True
    print(T)
    for i in range(1, rows):
        for j in range(1, cols):
            if j >= input[i - 1]:
                T[i][j] = T[i - 1][j] or T[i - 1][j - input[i - 1]]
            else:
                T[i][j] = T[i - 1][j]
    return T[rows - 1][cols - 1]
    """
   

def main():
    input = [1,4,6,7,8]
    total = 12
    print(subset_sum(input,total))

if __name__ == "__main__":
    main()