import csv 
import re 

path = "folderA/index.html"

sp = []
with open(path, 'r') as f:
    data = f.read()
    file_data = data.encode('utf-8')
    
    s = data.split('\n')
    
    for i in s:
        l = i.split(" ")
        if l != "":
            sp.append(l)
            

for i in sp:
    for j in i:
        if j != "":
            print(j)