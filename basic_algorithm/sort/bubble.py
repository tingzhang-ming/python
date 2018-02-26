

def bubble_sort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(i+1, l):
            if arr[j] < arr[i]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp


def bubble_sort_e(arr):
    l = len(arr)
    n = 0
    for i in range(l):
        change = False
        for j in range(i+1, l):
            n += 1
            if arr[j] < arr[i]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
                change = True
        if not change:
            break
    print n


def bubble_sort2(arr):
    l = len(arr)
    for i in range(l-1):
        for j in range(l-1-i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp


def bubble_sort2_e(arr):
    l = len(arr)
    n = 1
    for i in range(l-1):
        change = False
        for j in range(l-1-i):
            n += 1
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                change = True
        if not change:
            break
    print n


if __name__ == '__main__':
    arr = [5, 10, 3, 1, 7, 2, 8]
    arr2 = [1, 2, 3, 5, 7, 8, 10]
    bubble_sort2_e(arr2)
    print arr2
