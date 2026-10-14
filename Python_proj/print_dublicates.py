# print duplicates in string
str_input = input("enter the string")
list_in = list(str_input)
set_out = set()
my_list = []
count =0
for i in range(len(list_in)):
    for j in range (i+1, len(list_in)):
        if list_in[i] == list_in[j]:
            set_out.add(list_in[i])
        else:
            my_list.append(list_in[i])
        
        
print("".join(set_out))
print("".join(my_list))


    
            
            
        
        
    
    
    



