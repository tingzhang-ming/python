

def number_to_aaa(number):
    if number == 0:
        return "AAA"
    al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapAl = {i: al[i] for i in range(26)}
    res = []
    while number > 0:
        res.append(mapAl[number % 26])
        number /= 26
    while len(res) < 3:
        res.append('A')
    res.reverse()
    return "".join(res)


if __name__ == '__main__':
    print(number_to_aaa(149))
