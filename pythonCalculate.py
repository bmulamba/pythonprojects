print("THIS IS SIMPLE CALCULATE\n")

x = int(input("Put your Fist Number: "))
y = int(input("Put your Second Number: "))
op = input("Choose an Operator : ")

if op == '+' :
    print('Your result is: ', x + y)
    
elif op == '-' :
    print('Your result is: ', x - y)
    
elif op == '/' :
    print('Your result is: ', x / y)
    
elif op == '*' :
    print('Your result is: ', x * y)
    
else :
    print('Please put the right operator')