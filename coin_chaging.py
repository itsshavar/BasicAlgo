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
    print(min_coins2(input,total))
    
if __name__ == "__main__":
    main()