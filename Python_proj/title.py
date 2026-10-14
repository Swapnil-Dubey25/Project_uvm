import sys as s
from pprint import pprint

my_dict_1 = {}

s.stdout.write("Hello\n")
data_value = {"data": [2,5,6,7,8] , "value" : 25}

def square(x):
    result = x*x
    return result
     
    
if "data" in data_value:
    print(data_value["data"])
    data_value["data"] = list(map(lambda x:square(x), data_value["data"]))
    
if "data" in data_value:
    for i,j in enumerate(data_value["data"]):
     print(f"value of i is {i}and j is {j}")
     my_dict_1[i] = j

pprint(data_value)
pprint(my_dict_1)

# file =  open("file.txt", 'w+')
# file.write("hello_World")
# file.seek(0)
# print(file.read())

