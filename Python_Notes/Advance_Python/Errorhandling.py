#syntax error
#print("Hello"
#runtime error
#print(100/0) #ZeroDivisionError: division by zero
#number=[1,2,3]
#print(number[5])#IndexError: list index out of range

#logical error
'''
def add(a,b):
    return a-b
print(add(10,5))# out put getting error
'''
#Exception= to handle runtime error

#handle it 
'''
try
except
else
finally
'''
try:
    x = int(input("Enter Number: "))
    result =(10/x)
except ZeroDivisionError:
    print("you cant devide by zero")  
except ValueError:
    print("Provide value in number")
except TypeError:
    print("you can not divide with string")
else:
    print("result:" , result )
finally:
    print("work is completed")

