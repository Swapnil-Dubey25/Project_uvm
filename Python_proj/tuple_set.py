input_list = ["apple","mango","boat","shoes","wow","mumbai","race"]
output_list = []
variable_list = []
count =0
for value in range(len(input_list)):
    length_val = len(input_list[value])
    if length_val not in variable_list:
        temp = []
        for ch in input_list:
            if length_val == len(ch):
                temp.append(ch)
        output_list.append(tuple(temp))
    variable_list.append(length_val)

print(output_list)




    