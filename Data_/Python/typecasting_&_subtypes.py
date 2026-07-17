'''
typecasting  - conversion of one data type into another 

2 Methods
1 - implicit- python itself converts one DT to another 

2 - Explicit -  user converts one dat ato another
'''
# name= "john"
# print(type(name))

# age=23
# print(type(age))

#implicit
# num1=10
# num2=10.1
# print(type(num1))
# print(type(num2))
# print(num1+num2)
# print(type(num1+num2))

#explicit
num1="10"
num2=10.1
print(type(num1))
print(type(num2))

num1=int(num1)
print("after conversion",type(num1))
print(num1+num2)
print(type(num1+num2))