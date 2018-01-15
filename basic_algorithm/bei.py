

n = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]
W = 5

# d[i+1][j] = max{d[i][j], d[i][j-w[i]]+v[i](j>=w[i])}


def solve():
    d = [[0] * (W + 1) for i in range(n + 1)]
    for i in range(n):
        for j in range(1, W+1):
            if j >= w[i]:
                d[i+1][j] = max(d[i][j], d[i][j-w[i]]+v[i])
            else:
                d[i+1][j] = d[i][j]
    print d
    print d[n][W]


if __name__ == '__main__':
    solve()


