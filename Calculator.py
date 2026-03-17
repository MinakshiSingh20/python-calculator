def add (a,b):
    return a+b

def sub(a,b):
    return a-b

def multipy(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error! Division by 0 is not allowed"
    return a/b

# taking inputs from the user
num1= float(input("Enter first number:"))
num2= float(input("Enter second number:"))

print("select operation:")
print("1. addition:")
print("2. substraction:")
print("3. multiplication:")
print("4. division:")

choice = input("Enter choice (1/2/3/4):")

#performing the selected operation
if choice == '1':
    print("result:", add(num1,num2))

    
elif choice == '2':
    print("result:", sub(num1,num2))

elif choice == '3':
    print("result:", multipy(num1,num2))

elif choice == '4':
    print("result:", divide(num1,num2))


else:
    print("Invalid choice")

          



    