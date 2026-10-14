
# reverse string

input_string = input("Enter the string to reverse")
my_list = list(input_string)
string_value = len(input_string)
print(f"value of list{my_list} and length {string_value}\n")
j = string_value-1
print(j)
for i in range(4):
    temp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = temp
    j = j-1

print(my_list)

rev_string = ""

for i in my_list:
    rev_string = rev_string+i

print(rev_string)
    
#reverse_string = "".join(my_list)
#print(reverse_string)

    
    
    