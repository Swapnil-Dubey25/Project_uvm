input = [1,2,3,4,5,6]
count_even = 0
count_odd = 0
for ch in input:
    if int(ch) % 2==0:
        count_even = count_even + int(ch)
    else:
        count_odd = count_odd + int(ch)
print(f"sum of even elements is {count_even} and odd elements is {count_odd}")