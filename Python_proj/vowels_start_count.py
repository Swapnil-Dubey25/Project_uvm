input_value = "apple is a orange fruit"
count =0
for ch in input_value.split():
    if ch[0].lower() in "aeiou":
            count = count+1

print(count)