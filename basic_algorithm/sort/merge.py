

def sort(l):
    ll = len(l)
    tmp = [0] * ll
    _sort(l, 0, ll-1, tmp)


def _sort(l, left, right, tmp):
    if left < right:
        mid = (left + right) / 2
        _sort(l, left, mid, tmp)
        _sort(l, mid+1, right, tmp)
        merge(l, left, mid, right, tmp)


def merge(l, left, mid, right, tmp):
    i = left
    j = mid + 1
    t = left
    while i <= mid and j <= right:
        if l[i] < l[j]:
            tmp[t] = l[i]
            i += 1
        else:
            tmp[t] = l[j]
            j += 1
        t += 1
    while i <= mid:
        tmp[t] = l[i]
        i += 1
        t += 1
    while j <= right:
        tmp[t] = l[j]
        j += 1
        t += 1
    for i in range(left, right+1):
        l[i] = tmp[i]


def main():
    l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort(l)
    print l


if __name__ == '__main__':
    main()
