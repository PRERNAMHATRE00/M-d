#sum of even numb  upto 50
# sum=0
# for i in range(0,51):
#     if i%2==0:
#         sum+=i
        
# print(sum)

#first 20 numb and their square

# for i in range(0,21):
#     square=i**2
#     print(i,square)

# sum of first 10 odd numb -while loop

# for i in range(0,11):
#     if i%2==1:
#         sum=i
#         print(i)
# print(sum)

# i=0
# sum=0
# while i<=20:
#     if i%2!=0:
#         sum+=i
        
#     i+=1
# print(i," ",sum)

#numb divisible  by 8 and 12 upro 100
# for i in range(0,101):
#     if i%8==0 and i%12==0:
#         print(i)
# print()

#billing system at supemarket

while True:
    name=input("Enter customer no: ")
    total=0
    while True:
        quantity =float(input("Enter Quantity : "))
        amount=float(input("Enter Amount : "))
        total=amount*quantity
        repeat= input(" Repeat : ")
        if repeat=="no" or repeat=="NO":
            break
    print("- "*40)
    print(name)
    print(total)
    print(" *"*40)

    repeat1= repeat= input(" Repeat : ")
    if repeat=="no" or repeat=="NO":
            break
