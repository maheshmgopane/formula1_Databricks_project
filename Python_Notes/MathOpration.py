num_1=float(input("Enter the first number: "))
num_2=float(input("Enter the second number: "))

choice=input("Enter the operation you want to perform (+, -, *, /): ")
if choice=='+':
    result=num_1+num_2
    print("The sum is: ", result)
elif choice=='-':
    result=num_1-num_2
    print("The difference is: ", result)
elif choice=='*':
    result=num_1*num_2
    print("The product is: ", result)
elif choice=='/':   
    if num_2!=0:
        result=num_1/num_2
        print("The quotient is: ", result)
    else:
        print("Error: Division by zero is not allowed.")    