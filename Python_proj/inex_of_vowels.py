index = "education"
my_list = list(index)
final = []
for ch in range(len(my_list)):
    if my_list[ch].lower() in "aeiou":
        final.append(ch)

print(final)        
       
        

