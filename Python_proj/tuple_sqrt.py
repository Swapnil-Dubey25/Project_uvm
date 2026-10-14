input_t = (1,2,3,4)
my_list = []
for num in range(len(input_t)):
    my_list.append(input_t[num]*input_t[num])
    
print(tuple(my_list))
    
    