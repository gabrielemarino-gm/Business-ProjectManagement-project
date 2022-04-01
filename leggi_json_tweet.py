import os
import json
import re
import regex
from os import walk


myPath = 'D:\\Università\\Magistrale\\Primo anno\\Business\\The Chad 2\\Companies_Tweet-20220324T151322Z-001\\Companies_Tweet\\google'

files = os.listdir(myPath)
os.chdir(myPath)
for filename in files:
    jsonFile = open(filename, encoding="utf-8")
    data = json.load(jsonFile)    
    for i in range(len(data)):
        match = re.findall(r'\bface\b', data[i]["text"])
        if match: # this means: if match exists
            print("\n")
            print(data[i]["text"])
    