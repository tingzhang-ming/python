

n = 3
w = [3, 4, 2]
v = [4, 5, 3]
W = 7

# d[i+1, j] = max{d[i,j], d[i+1, j-w[i]]+v[i](j>=w[i])}


def solve():
    d = [[0] * (W+1) for i in range(n+1)]
    for i in range(n):
        for j in range(1, W+1):
            if j < w[i]:
                d[i+1][j] = d[i][j]
            else:
                d[i+1][j] = max(d[i+1][j-w[i]]+v[i], d[i][j])
    print d[n][W]

if __name__ == '__main__':
    solve()


