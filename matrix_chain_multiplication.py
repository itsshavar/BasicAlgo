def print_(m):
    for i in m:
        print(i)
def matrix_chain(p):
    n = len(p)
    m = [[0]*n]*n
    s = [[0] * n ] * n
    for l in range(2,n):
        for i in range(1,n-l+1):
            j = i+l-1
            m[i][j] = float('inf') 
            for k in range(i,j):
                print(m[i][k],m[k+1][j],p[i-1]*p[k]*p[j])
                q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m,s


def main():
    matrices = [4, 2, 3, 5, 3]
    print(matrix_chain(matrices)[0])

if __name__ == "__main__":
    main()