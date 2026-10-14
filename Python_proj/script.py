
file1 = open("text1", "w+")
file1.write("hello world India\n")
file1.write("bangalore, karnataka\n")
file1.close()

file1 = open("text1", "r+")
file2 = open("text2", "w+")

for value in file1:
    file2.write(value)
    
file1.close()
file2.close()
