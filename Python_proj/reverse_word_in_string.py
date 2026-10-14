
input = "python is fun"
my_list= []
#print(input.split())

for ch in input.split():
    my_list.append(ch[::-1])
    
print(" ".join(my_list))