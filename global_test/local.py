

createVar = locals()

listTemp = range(1,10)
for i, s in enumerate(listTemp):
    createVar['a' + str(i)] = s

print a1, a2, a3