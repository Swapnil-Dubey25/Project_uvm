input = "programming"
set_r = set()
set_nr = set()
for ch in input:
    if input.count(ch) == 1:
        set_nr.add(ch)
    else:
        set_r.add(ch)
        
print(f"repeating {" ".join(set_r)} and non repeating {" ".join(set_nr)} characters ")