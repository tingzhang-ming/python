
def sameDicts(dict1, dict2):
    if len(dict1) != len(dict2):
        return False
    key1 = dict1.keys()
    key2 = dict2.keys()
    for i, key in enumerate(key1):
        if key2[i] != key:
            return False
    for k, v in dict1.items():
        if dict2[k] != v:
            return False
    return True

if __name__ == "__main__":

    d1 = {"a1":"b1","a2":"b2","s":"2"}
    d2 = {"a1": "b1", "a2": "b2","s":"s"}
    print sameDicts(d1, d2)
d1 = {"a1":"b1","a2":"b2"}