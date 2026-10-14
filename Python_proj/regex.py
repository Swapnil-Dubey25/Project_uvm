# -----------------------------------------------------------------------------------------------
                      #using sys module
# -----------------------------------------------------------------------------------------------
# import sys
# if len(sys.argv) < 2:
#     print("error expecting 3 arguments as file")
# else:
#     print("argv successful") 

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------
                        #using arsparse function
# -----------------------------------------------------------------------------------------------
# import argparse

# parser = argparse.ArgumentParser( description= "We are running the python script")

# parser.add_argument("--value", type= int,default = 10)
# parser.add_argument("data",type = int)
# parser.add_argument("--content",type = int,default= 20)
 
# args = parser.parse_args()

# print(f"value = {args.value}, data = {args.data}, content = {args.content}")

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------
                         # kargs:
#------------------------------------------------------------------------------------------------


# def values(**val):
#     sumer = 0
#     for i in val:
#         #sum(val[i])
#         sumer = sumer + val[i]
#     print(sumer)

# values(aplha=100,beta=200,gamma=300)



#-----------------------------------------------------------------------------------------------
                         #  factorial of a number:
#------------------------------------------------------------------------------------------------
# def fact(num):
#     if num==1:
#         return 1
#     else:
#      return num * fact(num-1)

# value = int(input("enter the number"))
# print(f"factorial of the number {value}:{fact(value)}")

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------
                         #  Reverse the string using python:
#------------------------------------------------------------------------------------------------
# def reverse_string(value):
#     if len(value) <=1:
#         return value
#     else:
#         return reverse_string(value[1::]) + value[0]
    

# input_s = "Python"
# print(reverse_string(input_s))
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------
                            # sum of digits using recursion: 
# -----------------------------------------------------------------------------------------------    

# def func_add(val):
#     if len(val)==1:
#         return int(val)
#     else:
#          return  func_add((val[1::])) + int(val[0])

# input_value = input("enter the digit")
# print(f"sum of digit {input_value} : {func_add(input_value)}")

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------
                            # count occurance of a value in the string
# -----------------------------------------------------------------------------------------------

# def search_value(list_s,value):
#     count = 0
#     if len(list_s) == 0:
#         return count
#     if value == list_s[0]:
#         count = count + 1
#         return count + search_value(list_s[1::],value) 
#     else:
#         return count + search_value(list_s[1::],value) 


# my_list = [1,2,2,2,4,2]
# value = 2
# print(search_value(my_list,value))

# -----------------------------------------------------------------------------------------------
               # max and min using recursion
# -----------------------------------------------------------------------------------------------

# def max_min_func(list_value):
#         if len(list_value) == 1:
#             return list_value[0],list_value[0]
        
#         max_value,min_value = max_min_func(list_value[1::])
        
#         current_index = list_value[0]
        
#         if(max_value < current_index):
#             final_max_value = current_index
#         else:
#             final_max_value = max_value
#         if(min_value > current_index):
#             final_min_value = current_index
#         else:
#             final_min_value = min_value
            
#         return final_max_value, final_min_value

# my_list = [1,2,6,7,8,9,20]
        
# print(f"(max,min): {max_min_func(my_list)}")

# -----------------------------------------------------------------------------------------------
               # count digits using recursion
# -----------------------------------------------------------------------------------------------

# def count_value(value):
#      count = 0
#      if len(value) == 1:
#          count = 1
#          return count
#      else:
#          count = count + 1
#          return count + count_value(value[1::])


# my_digit = "56748"
# print(f"total number of digit:{count_value(my_digit)}")

# -----------------------------------------------------------------------------------------------
               # fibonacci number of a number         
# -----------------------------------------------------------------------------------------------

# def fibo_nacci(num):
#     if num == 1:
#         return 1
#     if num == 0:
#         return 0
#     else:
#         return fibo_nacci(num-1) + fibo_nacci(num-2)

# value = int(input("Enter the number who's fibonacci is required"))
# print(f"the fibonacci number {value} is {fibo_nacci(value)}")


# -----------------------------------------------------------------------------------------------