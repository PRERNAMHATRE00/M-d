#For loop
# for i in range(1,8,2):
#     print("HEY!!",i)
#for i in range(1,8):
#     print("HEY!!",i)

#Table of 9
# n=int(input("enter number for table "))
# for i in range(1,20,2):
#     print(n,"x",i,"=",n*i)

#While Loop
# n=0
# while n<=10:
#     print("Hi",n)
#     n=n+2 #n +=1

#TABLE
# n=1
# v=5
# while n<=10:
#     print(v,"X",n," = ",v*n)
#     n+=1

#while True
# while True:
#     num1=int(input("num1 ="))
#     num2= int(input("num2 "))
#     print(num1+num2)

#     repeat = input("Do u want to stop type Y")
#     if repeat =="Y":
#         break

#Nested loop

# i=0
# for i in range(1,4):
#     for j in range(1,11):
#         print(j,end=" ")
#     print("__ ")

#reverse
# for i in range(1,3):
#     for j in range(10,0,-1):
#         print(j,end="")
#     print()


#PATTERN
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
        
#     print()


#Star pattern
# for i in range(1,11):
#     for j in range(1,i+1):
#         print(" * ",end="")
#     print()

#reverse pattern
# for i in range(0,6):
#     for j in range(6,i,-1):
#         print(j,end=" ")
#     print()

# for i in range(1,4):
#     for j in range(4,i,-1):
#         print("*",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,7-i):
#      print("*",end="")
#     print()

#Triangle
# row=5
# for i in range(1,row +1):
#     print(" "*(row-i),end="")
#     print("* "*i)

#

# for i in range(0,5):
#     for j in range(0,i):
#         print(i,end=" ")
#     print()

#Floyd's Triangle
# num=1
# for i in range(1,5):
#     for j in range(1,i-1):
#         print(num,end=" ")
#         num+=1
#     print()


# num=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()

#Continuous Alphabet Pattern
# for i in range(1,6):
#     for j in range (1,i+1):
#         print(chr(64 +j),end="")
#     print()



#for loop in condition
# for i in range(0,12):
#     if i <=3:
#         print(i,"  top song")
#     else:
#         print(i)

# for i in range(0,1000):
#     if i % 8==0 and i % 12 ==0:
#         print(i,end=" ")


#While  loop in condition
# i=0
# while i<10:
#     if i<=3:
#      print(i,"Top song")
#     else:
#        print(i)
#     i+=1

#Break and contionue

# for i in range(1,21):
#     if i==6 or i==9:
#         continue
#     else:
#         print(i,end=" ")

# for i in range(1,21):
#     if i==6 and i==9:
#         continue
#     else:
#         print(i,end=" ")

for i in range(1,21):
    if i==6 or i==9:
        break
    else:
        print(i,end=" ")
        print("\nHi\n")

print("Thank you")