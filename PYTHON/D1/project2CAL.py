a=float(input("enter first number:"))
operator=input("Enter operator:")
b=float(input("enter second number:"))


if operator=="+":
    print("result:", a+b)
elif operator=="-":
    print("result:", a-b)
elif operator=="*":
    print("result:", a*b)
elif operator=="/":
    print("result:", a/b)
elif operator=="%":
    print("result:", a%b)
else:
    print("invalid operator")




