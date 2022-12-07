"""
Program : Calculator.py
Author : VABSYO
Purpose of Program : To make a Calculator using Python programming language
"""
print("A WORLD CLASS, ONLY ONE MADE EVER, BEST-OF-THE-BEST CALCULATOR :- \n")

a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def prod(x,y):
    return x*y

def div(x,y):
    return x/y

def exp(x,y):
    return x**y

def rem(x,y):
    return x%y

def quo(x,y):
    return x//y

print("Operations you can perform :- \n\t 1. +(Addition) \n\t 2. -(Subtraction) \n\t 3. *(Multiplication) \n\t 4. /(Division) \n\t 5. **(Exponent(a to the power b)) \n\t 6. %(Remainder) \n\t 7. //(Floor division(To get the quotient))\n\t ")

option = input("Enter the operator according to the operation you want to perform : ")

if(option == "+"):
    print("The addition of ",a, "and ",b, "gives : ",add(a,b))

elif(option == "-"):
    print("The subtraction of ",a, "and ",b, "gives : ",sub(a,b))

elif(option == "*"):
    print("The multiplication of ",a, "and ",b, "gives : ",prod(a,b))

elif(option == "/"):
    print("The division of ",a, "and ",b, "gives : ",div(a,b))

elif(option == "**"):
    print("The exponential of ",a, "and ",b, "gives : ",exp(a,b))

elif(option == "%"):
    print("The remainder of ",a, "divided by ",b, "is : ",rem(a,b))

elif(option == "//"):
    print("The floor division of ",a, "and ",b, "gives : ",quo(a,b))

else:
    print("The symbol you imput is wrong, please try again!")