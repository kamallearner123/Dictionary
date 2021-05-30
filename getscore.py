import os
import re
import json

dirs = list(filter(lambda x: not x.startswith(".") and os.path.isdir(x) ,os.listdir()))
print(dirs)

for name in dirs:
    count = 0
    files = list(filter(lambda x: re.search(r"\d{4}\-\d{2}\-\d{2}", x), os.listdir(name)))
    
    for fname in files:
        with open(name+"/"+fname) as f:
            d = json.loads(f.read())
            count += len(d)
    print("Score of {} is {}".format(name, count))

