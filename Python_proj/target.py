
list_output = [2,5,8,6,5,5,4,2]
target = 10
my_list = []
for i in range(len(list_output)):
    for j in range(i+1, len(list_output)):
        if(list_output[i] + list_output[j] == target):
            print(f"{list_output[i]}, {list_output[j]}")
            my_list.append((list_output[i], list_output[j]))
            
print(my_list)