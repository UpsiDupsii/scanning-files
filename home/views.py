from django.shortcuts import render
from django.urls import reverse
import csv
import re
import os

sp = []
vul_context = {
    "file_name": set(),
    "vulnerability": set(),
    "matcher": set(),
    "id": set(),    
    "type": set(),
}
fname = []

vul_data = []
csv_data = []


def index(request):
    if request.method == 'POST' and request.FILES.getlist('myfile'):
        myfiles = request.FILES.getlist('myfile')
        with open("data/test.csv", "r") as f:
            reader = csv.reader(f)
            lst = list(reader)
            for i in lst:
                sp2 = i[7].split("\n")
                csv_data.append(sp2)
            for file in myfiles:
                file_extension = os.path.splitext(file.name)[1].lower()
                if file_extension == '.txt':
                    data = file.read()
                    file_data = data.decode('utf-8')
                    print("+++++++++++++++++++++")
                    s = file_data.split(" ")
                    print(s)
                    for i in s:
                        p = i.split("\n")
                        for k in p:
                            vul_data.append(k)
                    for k in vul_data:
                        for l in csv_data:
                            for j in l:
                                if j != "" and k != "":
                                    #Pattern with starting spaces
                                    if j[0] == " ":
                                        j = j.replace(" ", "")
                                        if '\\' in j:
                                            j = j.replace("\\", "\\\\")
                                            if j in k or j == k:
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("word")
                                            if re.search(rf"""{j}""", f"""{file_data}""") or re.search(rf"""{j}""", f"""k"""):
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("regex")
                                        else:
                                            if j in k or j == k:
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("word")
                                            if re.search(rf"""{j}""", f"""{file_data}""") or re.search(rf"""{j}""", f"""k"""):
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("regex")                                               
                                    #Pattern without starting space
                                    if j[0] != " ":
                                        if '\\' in j:
                                            j = j.replace("\\", "\\\\")
                                            if j in k or j == k:
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("word")
                                            if re.search(rf"""{j}""", f"""{file_data}""") or re.search(rf"""{j}""", f"""k"""):
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("regex")
                                        else:
                                            if j in k or j == k:
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("word")
                                            if re.search(rf"""{j}""", f"""{file_data}""") or re.search(rf"""{j}""", f"""k"""):
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("regex") 
                                    
                if file_extension == '.html':
                    data = file.read()
                    file_data = data.decode('utf-8')
                    s = file_data.split(" ")
                    for i in s:
                        p = i.split("\n")
                        for k in p:
                            vul_data.append(k)
                    for k in vul_data:
                        for l in csv_data:
                            
                            for j in l:
                                if j != "" and k != "":
                                    #Pattern with starting spaces
                                    if j[0] == " ":
                                        j = j.replace(" ", "")
                                        if '\\' in j:
                                            j = j.replace("\\", "\\\\")
                                            if j in k or j == k:
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("word")
                                            if re.search(rf"""{j}""", f"""{file_data}""") or re.search(rf"""{j}""", f"""k"""):
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("regex")
                                        else:
                                            if j in k or j == k:
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("word")
                                            if re.search(rf"""{j}""", f"""{file_data}""") or re.search(rf"""{j}""", f"""k"""):
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("regex")                                               
                                    #Pattern without starting space
                                    if j[0] != " ":
                                        if '\\' in j:
                                            j = j.replace("\\", "\\\\")
                                            if j in k or j == k:
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("word")
                                            if re.search(rf"""{j}""", f"""{file_data}""") or re.search(rf"""{j}""", f"""k"""):
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("regex")
                                        else:
                                            if j in k or j == k:
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("word")
                                            if re.search(rf"""{j}""", f"""{file_data}""") or re.search(rf"""{j}""", f"""k"""):
                                                vul_context["file_name"].add(file)
                                                vul_context["vulnerability"].add(j)
                                                vul_context["matcher"].add(k)
                                                vul_context["id"].add(l[0])
                                                vul_context["type"].add("regex")
                                                
                                                        
                                            
    print(vul_context)
    return render(request, 'index.html')

def vulnerability(request):
    with open("data/test.csv", "r") as file:
        reader = csv.reader(file)
        lst = list(reader)
        for i in lst:
            sp = i[7]
            
    return render(request, 'vulnerability.html', {"vul_context": vul_context})