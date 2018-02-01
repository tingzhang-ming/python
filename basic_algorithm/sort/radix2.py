# encoding: utf-8


def get_gao_wei(arr):
    """ 获取最大数的位数 """
    max_num = max(arr)
    res = 1
    while max_num/10 > 0:
        res += 1
        max_num /= 10
    return res


def _radix_sort_msd(arr, r):
    if r == 0:
        return
    cheng = 10 ** (r-1)
    bucket = [[] for _ in range(10)]
    l = len(arr)
    for i in range(l):
        wei = (arr[i]/cheng) % 10
        bucket[wei].append(arr[i])
    for bi in range(10):
        if len(bucket[bi]) > 1:
            _radix_sort_msd(bucket[bi], r-1)
    del arr[:]
    for bi in bucket:
        arr.extend(bi)


def radix_sort_msd(arr):
    r = get_gao_wei(arr)
    _radix_sort_msd(arr, r)


def main():
    arr = [170, 45, 75, 90, 2, 24, 802, 66, 2]
    radix_sort_msd(arr)
    print arr
# [2, 2, 24, 45, 66, 75, 90, 170, 802]


if __name__ == '__main__':
    main()

