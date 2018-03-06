import pandas
import seaborn


h_df = pandas.read_csv("/root/github/python/pandas/a.csv")
# print h_df.head(3)
for i in dir(h_df['age']):
    if i.startswith("_"):
        continue
    print i
print [i for i in h_df['age']]
print type(h_df['age'])
seaborn.distplot(h_df['age'])
