
def count_sort(arr):
    l = len(arr)
    c = [0] * 1000
    for i in range(l):
        c[arr[i]] += 1
    for ci in range(1, 1000):
        c[ci] += c[ci-1]
    res = [0] * l
    for i in range(l):
        res[c[arr[i]]-1] = arr[i]
        c[arr[i]] -= 1
    for i in range(l):
        arr[i] = res[i]


def main():
    arr = [4, 5, 3, 1, 7, 2, 8]
    count_sort(arr)
    print arr


if __name__ == '__main__':
    main()
