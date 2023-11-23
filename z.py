from django.shortcuts import render
from django.urls import reverse
import csv
import re

file_names = {
    'name': 'none',
}
text_data = []
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
                    data = file.read()
                    data1 = data.decode('utf-8')
                    print(data1)
                    print("++++++")
                    file_data = data = data.decode('utf-8')
                    sp = file_data.split(" ")
                    for a in csv_data:
                        for j in a:
                            for k in sp:
                                if j != "":
                                    if j[0] == " ":
                                        j = j.replace(" ", "")
                                        if j == k:
                                            print(j)
                                            print(k)
                                            print(file)
                                            print(i[0])
                                            print("word")
                                            print("________________________")
                                        if re.search(rf"""{j}""", data):
                                            print(j)
                                            print(k)
                                            print(file)
                                            print(i[0])
                                            print("regex")
                                            print("________________________")
        
    return render(request, 'index.html')

def vulnerability(request):
    with open("data/test.csv", "r") as file:
        reader = csv.reader(file)
        lst = list(reader)
        for i in lst:
            sp = i[7]
            
    return render(request, 'vulnerability.html')