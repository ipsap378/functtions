def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
num = int(input("enter a number"))
if num < 0:
    print ("sorry factorial doesnt exist for a negitive number")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    print("the factorial of" , num , "is " , factorial(num))
    