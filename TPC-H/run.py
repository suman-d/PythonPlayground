import pandas

df1 = pandas.read_csv("hammerdb_16GB.log", delimiter=":")

l = list(df1.ix[:, "14"])

result = []
for i in l:
    if str(i).startswith("query"):
        result.append(i)
    if str(i).startswith("Completed"):
        result.append(i)
result.sort()


for i in result:
    print str(i).split("completed in ")[-1]

