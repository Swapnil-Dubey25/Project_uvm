input_t = (5,12,18,3,25)
count = 0

for num in range(len(input_t)):
    if input_t[num] > 10:
        count = count+1
print(count)