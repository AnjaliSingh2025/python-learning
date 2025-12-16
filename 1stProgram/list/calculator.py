print('''
+ Addition
- Substraction
* Multiplication
/ Division 
      ''')
num1=int(input("Enter the number1:-"))
num2=int(input("Enter the number2:-"))
opr=input("Enter the operation:+,-,*,/")
if opr=="+":
    print(num1+num2)
elif opr=="-":
   print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else :
    print("Invalid operation entered")