import random


# nlogn
def quick_sort(arr, _left, _right):
    left = _left
    right = _right
    if left <= right:
        while left != right:
            tmp = arr[left]
            while left < right and arr[right] >= tmp:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= tmp:
                left += 1
            arr[right] = arr[left]
            arr[left] = tmp
        quick_sort(arr, _left, left-1)
        quick_sort(arr, right+1, _right)


def quick_sort2(arr, _left, _right):
    left = _left
    right = _right
    if left <= right:
        random_index = random.randint(left, right)
        tmp = arr[left]
        arr[left] = arr[random_index]
        arr[random_index] = tmp
        while left != right:
            tmp = arr[left]
            print tmp
            while left < right and arr[right] >= tmp:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= tmp:
                left += 1
            arr[right] = arr[left]
            arr[left] = tmp
        quick_sort(arr, _left, left-1)
        quick_sort(arr, right+1, _right)


def main():
    arr = [5, 10, 3, 1, 7, 2, 8]
    quick_sort(arr, 0, len(arr)-1)
    print arr


if __name__ == '__main__':
    main()

