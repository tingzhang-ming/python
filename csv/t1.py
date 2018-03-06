import csv

datas = [['name', 'age'],
         ['Bob', 14],
         ['Tom', 23],
         ['Jerry', '18']]

with open('/root/github/python/pandas/a.csv', 'w') as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)

    # writer.writerows(datas)