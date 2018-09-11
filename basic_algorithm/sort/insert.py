

def insert_sort(arr):
    l = len(arr)
    for i in range(1, l):
        if arr[i-1] > arr[i]:
            tmp = arr[i]
            j = i
            while j > 0 and arr[j-1] > tmp:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = tmp


if __name__ == '__main__':
    arr = [4, 7, 8, 1, 5, 2, 3]
    insert_sort(arr)
    print(arr)
