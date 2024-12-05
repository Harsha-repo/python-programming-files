def add(num1 , num2):
    return num1+ num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide (num1,num2):
    if num2==0 :
        print('enter number greater than zero')
    else:
      return num1/num2
    
def calculator():
    print('1.add\n2.subtract\n3.multpliaction\n4.division')
   
    while True :
        choice = int(input('enter your choice opration:'))
        if (choice =='5') :
            print('exiting the calculator')
            break
        num1=int(input('enter first number: '))
        num2 = int(input('enter second number: '))
    
        if choice=='1' :
          result=add(num1,num2)
          print('the sum is :',result)
        elif choice == '2' :
         result=subtract(num1,num2)
         print('difference is : ',result)
        elif choice == '3' :
          result = multiply(num1,num2)
          print('product is : ',result)

        elif choice=='4' :
          result = divide(num1,num2)
          print('the quotient is : ',result)

        else :
          print('invalid input')

calculator() 




