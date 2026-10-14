input = [1,2,3,4]

length = len(input)
result = [1]* length
print(result)
i=0
while i< length:
    value =1
    j = 0 
    while j < length:
        if i!=j:
             value = value * input[j]
             j = j+1
    result[i] = value
    i =i+1

print(result)
