

n = 4
m = 4
s = 'abcd'
t = 'becd'

'''
d[i+1][j+1] = max{d[i][j]+1, d[i+1][j], d[i][j+1]},  when s[i+1] == t[j+1]
d[i+1][j+1] = max{d[i+1][j], d[i][j+1]},  when s[i+1] != t[j+1]
'''


def solve():
    d = [[0] * (m+1) for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                d[i+1][j+1] = max(d[i][j]+1, d[i][j+1], d[i+1][j])
            else:
                d[i+1][j+1] = max(d[i][j + 1], d[i + 1][j])
    print d[n][m]


if __name__ == '__main__':
    solve()

