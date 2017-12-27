# __*__ coding:utf-8__*__

a = open("/root/github/python/file_test/test.txt")

a.seek(1, 0)

print a.tell()
a.seek(2, 1)
print a.readline()
print a.tell()
# print a.read()
a.close()
