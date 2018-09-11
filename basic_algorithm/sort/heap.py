

def heap_sort(arr):
    l = len(arr)
    for i in range(int(l / 2 - 1), -1, -1):
        addjust_heap(arr, i, l)
        # print(arr)
    for j in range(l-1, 0, -1):
        arr[j] = arr[j] ^ arr[0]
        arr[0] = arr[j] ^ arr[0]
        arr[j] = arr[j] ^ arr[0]
        addjust_heap(arr, 0, j)


def addjust_heap(arr, i, length):
    tmp = arr[i]
    k = 2 * i + 1
    while k < length:
        if k + 1 < length and arr[k+1] > arr[k]:
            k += 1
        if arr[k] > tmp:
            arr[i] = arr[k]
            i = k
        else:
            break
        k = 2 * k + 1
    arr[i] = tmp


def t1():
    arr = [4, 7, 8, 1, 5, 2, 3]
    addjust_heap(arr, 0, len(arr))
    print(arr)


def main():
    arr = [4, 5, 3, 1, 7, 2, 8]
    heap_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()

