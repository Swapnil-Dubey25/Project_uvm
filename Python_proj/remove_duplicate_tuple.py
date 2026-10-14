
input_t =  (1,2,2,3,4,4,5)

new_set = set()
my_list = []

for num in input_t:
    if num not in new_set:
        new_set.add(num)
        my_list.append(num)
        
print(tuple(my_list))
        