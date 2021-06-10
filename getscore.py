#!/bin/python3
import os
import re
import json
import datetime
from PyDictionary import PyDictionary

dictionary = PyDictionary()

new_words = []
dirs = list(filter(lambda x: not x.startswith(".") and os.path.isdir(x) and not "bck" in x,os.listdir()))
print(datetime.date.today())
wordslist = []
for name in dirs:
    count = 0
    files = list(filter(lambda x: re.search(r"\d{4}\-\d{2}\-\d{2}", x), os.listdir(name)))
    
    for fname in files:
        with open(name+"/"+fname) as f:
            d = json.loads(f.read())
            count += len(d)
            curr_list = [key.capitalize()+" = "+val for key, val in d.items()]
            new_words.extend(list(d.keys()))
            wordslist.extend(curr_list)
    print("%-30s:%3d"%(name+"'s score", count))
print("==== Dictionary words ====")
wordslist.sort()
list(map(print,wordslist))

finalDict = open("Dictionary.txt","w")
list(map(lambda word: finalDict.write("\nWord: %s\n%s\n"%(word,dictionary.meaning(word.split("=")[0].strip()))+"\n\n"),wordslist))
#list(map(lambda line: finalDict.write(line+"\n"),wordslist))
finalDict.close()
