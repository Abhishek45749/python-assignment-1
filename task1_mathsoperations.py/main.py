#Task 1: Perform Basic Mathematical Operations
#Input form User
num1=float(input("Enter First number:"))
num2=float(input("Enter Second number:"))
#Perform operations
addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
division=num1/num2 if num2!=0 else 0
"Cannot Divide by Zero "
# Display results
print("Addition:",addition)
print("Subtraction:",subtraction)
print("Multiplication:",multiplication)
print("Division:",division)