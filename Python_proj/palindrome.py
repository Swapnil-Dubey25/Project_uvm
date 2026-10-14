#palindrome_check
my_list =[] 
input_string = input("enter the string")
string_length = len(input_string)
current_length = string_length-1
for i in range(string_length):
    if i < current_length:
        if(input_string[i] == input_string[current_length-i]):
            my_list.append(1)
            print(my_list)
        else:
            my_list.append(0)
            print(my_list)
        #current_length = current_length-1
        
if(any(my_list)):
    print("string in a palindrome")
else:
    print("not a palindrome")
            


