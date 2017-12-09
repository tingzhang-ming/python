

with open('/a.txt', 'r') as reader, open('/b.txt', 'w') as writer:
    writer.write(reader.read())
