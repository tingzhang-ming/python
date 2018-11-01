

def string_to_array(s):
    if len(s) == 0:
        return []
    if s[0] != '[':
        raise Exception("Invalid input string")
    stack = []
    res = []
    for i in s:
        if i == ',':
            continue
        if i == '[':
            new = []
            if len(stack) > 0:
                stack[-1].append(new)
            stack.append(new)
        elif i == ']':
            res = stack.pop()
        else:
            stack[-1].append(int(i))
    return res


if __name__ == '__main__':
    s = '[1,2,3,[4,[5,6]]]'
    for i in string_to_array(s):
        print(i)
