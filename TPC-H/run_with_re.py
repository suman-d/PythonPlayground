import pandas
import re
#df1 = pandas.read_csv("hammerdb_16GB.log", delimiter=":")

filename = "hammerdb_16GB.log"


hammerregex = re.compile(r"Vuser (\d)*:query")
hammercompleteregex = re.compile(r"Completed 1 query set\(s\)")
with open(filename) as f:
    for i in f:
        if hammerregex.search(i) or hammercompleteregex.search(i):
            tmp = i.strip().split()
            print tmp[2], tmp[5]


