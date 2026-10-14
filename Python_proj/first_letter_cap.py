input = "welcome to programming"
my_list =[]
for ch in input.split():
    value = ch[0].upper()
    final_value = value + ch[1::]
    my_list.append(final_value)

print(" ".join(my_list))
    