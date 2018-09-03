# encoding: utf-8


def radix_sort_lsd(arr):
    l = len(arr)
    bucket = [[] for _ in range(10)]
    end = False
    cheng = 1
    while end is False:
        end = True
        for i in range(l):
            wei = (arr[i]/cheng) % 10
            if wei > 0 and end is True:
                # 这一位不是0, 继续计算
                end = False
            wei = int(wei)
            bucket[wei].append(arr[i])
        del arr[:]
        for bi in bucket:
            arr.extend(bi)
        bucket = [[] for _ in range(10)]
        cheng *= 10


def radix_sort_lsd2(arr):
    l = len(arr)
    bucket = [0] * 10
    temp = [0] * l
    end = False
    cheng = 1
    while end is False:
        end = True
        for i in range(l):
            wei = (arr[i]/cheng) % 10
            if wei > 0 and end is True:
                # 这一位不是0, 继续计算
                end = False
            wei = int(wei)
            bucket[wei] += 1
        for j in range(1, 10):
            bucket[j] += bucket[j-1]
        for i in range(l-1, -1, -1):
            wei = (arr[i]/cheng) % 10
            temp[bucket[wei]-1] = arr[i]
            bucket[wei] -= 1
        del arr[:]
        arr.extend(temp)
        bucket = [0] * 10
        cheng *= 10


def main():
    arr = [302, 20, 198, 32, 48]
    # radix_sort_lsd(arr)
    radix_sort_lsd(arr)
    print(arr)


if __name__ == '__main__':
    main()

