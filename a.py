
def t1():
    l = [1,3,5,7,9,11,13,15]
    for i in l:
        for j in l:
            for k in l:
                if i+j+k == 30:
                    return [i,j,k]
    return []

if __name__ == '__main__':
    print t1()