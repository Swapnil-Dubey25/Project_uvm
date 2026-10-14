
my_list = [10,70,30,20,40,50]

print(len(my_list))

for i in range(len(my_list)):
    for j in range(len(my_list)-i-1):
        if(my_list[j]> my_list[j+1]):
            temp = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = temp
            
print(my_list)
