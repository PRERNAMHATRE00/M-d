#prog to check if numb is postive
# num= int(input("enter any number : "))
# if num>0:
#     print("Number is postive")
# elif num==0:
#     print("Number is neutral")
# else:
#     print("Number is negative")

#check numb even or odd

# numb= int(input("Enter a number : "))
# if numb %2 ==0:
#     print("number is even")
# elif numb % 2==1:
#     print("number is odd")

# create calculator
# num1 = int(input("Enter num1 : "))
# num2 = int(input("Enter num2 : "))
# operation=input("to perform Calculation press: \n A : Addition [+] : \n S : Subtraction [-] \n M: Multiplication [x] \n D: Division : [/]\n M: Modolus (Return Remainder)[%] \n F: Floor Division(return Quotient)[//]  \n E: Exponentiation(power)[**]:  \n Operation : ")
# if operation == "A":
#     print("Addition : ",num1 + num2)
# elif operation == "S":
#     print("Subtraction : ",num1 - num2)
# elif operation == "M":
#     print("Multiplication : ",num1 * num2)
# elif operation == "D":
#     print("Division : ",num1 / num2)
# elif operation == "R":
#     print("Modolus : ",num1 % num2)
# elif operation == "F":
#     print("Floor Division : ",num1 // num2)
# elif operation == "E":
#     print("Exponentiation : ",num1 ** num2)
# else:
#     print("Invalid operation")

# #create area calculator
# print("   AREA   CALCULATOR   ")
# print("""Choice operation to perform
#       1 :  Area of Square
#       2 : Area of Rectangle
#       3 : Area of  Triangle
#       4 : Area of Circle """)

# choice= int(input("Enter your choice Between 1 to 4 : "))

# if choice==1:
#     print("1 :  Area of Square")
#     side=int(input("Enter value of side = "))
#     area=side+side # side **2
#     print("  Area of Square = ",area)
# elif choice==2:
#     print("2 : Area of Rectangle")
#     Leng=int(input("Enter value of Length = "))
#     brea=int(input("Enter value of Breath = "))
#     area=Leng*brea
#     print("  Area of Rectangle = ",area)
# elif choice==3:
#     print("3 : Area of  Triangle")
#     Leng=int(input("Enter value of Length = "))
#     brea=int(input("Enter value of Breath = "))
#     area=((1/2)*Leng*brea)
#     print("  Area of Triangle = ",area)
# elif choice==4:
#     print(" 4 : Area of Circle")
#     radius=int(input("Enter value of Radius = "))
#     area=((22/7)*radius*radius)  # 3.14 * radius **2 
#     print("  Area of Triangle = ",area)
# else:
#     print("Invalid operation")




#check passed letter is vowel or not

# word= input("Enter a word :")
# if word =="a" or word =="A" or word == "e" or word =="E" or word =="i" or word =="I" or word=="o" or word =="O" or word =="U" or word =="u"  :
#     print("IT\'s a Vowel")
# else:
#     print("It\'s Not a Vowel ")

#2method
# letter= input("enter a letter : ")
# if letter == "aeiou" or letter=="AEIOU":
#     print("It is a Vowel")
# else:
#     print("It is a Consonant")

#check if numb is single  digit numb, 2 digit numb and so on up to 5 digit
# print("Check if Number lies between 1 digit  to 5 digit  ")
# numb= int(input("Enter number between 1 digit  to 5 digit : "))
# if numb>=0 and numb<=9:
#     print("It is a 1 digit number")
# elif numb>=10 and numb<=99:
#     print("It is a 2 digit number")
# elif numb>=100 and numb<=999:
#     print("It is a 3 digit number")
# elif numb>=1000 and numb<=9999:
#     print("It is a 4 digit number")
# elif numb>=10000 and numb<=99999:
#     print("It is a 5 digit number")
# else:
#     print("ITs greater than 5 digit number")