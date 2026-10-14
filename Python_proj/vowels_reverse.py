str_input = input("enter the string input")
my_list = []
final = []
for ch in range(len(str_input)):
    if str_input[ch].lower() in "aeiou":
        my_list.append(str_input[ch])

my_list.sort(reverse=True)
print("".join(my_list))