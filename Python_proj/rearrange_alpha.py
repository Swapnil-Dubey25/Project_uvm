
# code to rearrange the characters of a string so that all alphabets characters appears before numeric charcters:
input = "p98ty7h6o5n"
list_num =[]
list_alpha = []

for ch in input:
    if ch.isalpha():
        list_alpha.append(ch)
    else:
        list_num.append(ch)

print("".join(list_alpha + list_num))
