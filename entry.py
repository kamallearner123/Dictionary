#!/bin/python3

import os
import re
import datetime
import json

names = list(filter(lambda x:not x.startswith(".") and not x.endswith(".py"), list(os.listdir())))
names.append("Exit")
while True:
    print("Enter name to enter words:")
    for index,name in enumerate(names):
        print("%2d. %s"%(index+1, name))
    index = int(input("Enter the option:"))
    if (index > len(names)-1):
        break
    print("Entering for %s", names[index-1])
    
    fname = names[index-1]+"/"+str(datetime.date.today())
    fd = open(fname,"w")
    d = dict()
    for i in range(5):
        word = input("Enter word:")
        meaning = input("Enter Meaning:")
        d[word] = meaning

    bck = open("bck/"+names[index-1]+"_"+str(datetime.date.today()), "a+")
    fd.write(json.dumps(d))
    bck.write(json.dumps(d))
    fd.close()
    bck.close()
    

print("Thank you!!!")

