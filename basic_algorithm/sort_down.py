
data = [3, 1, 5, 7, 2, 8, 4, 9, 6]


def insert_sort():
    l = len(data)
    for i in range(1, l):
        if data[i] > data[i-1]:
            guard = data[i]
            data[i] = data[i-1]
            j = i - 1
            while j >= 0 and guard > data[j]:
                data[j+1] = data[j]
                j -= 1
            data[j+1] = guard


def bubble_sort():
    l = len(data)
    for i in range(l):
        for j in range(i, l):
            if data[j] > data[i]:
                data[j], data[i] = data[i], data[j]


if __name__ == '__main__':
    # insert_sort()
    bubble_sort()
    print data

