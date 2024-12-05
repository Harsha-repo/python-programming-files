lower = int(input('enter lower limit :'))
upper = int(input('enter upper limit :'))
#num = int(input('enter your number : '))

for num in range (lower ,upper+1 ):
    if num > 1 :
         for i in range (2,num) :          # for else loop;
              if num%i==0 :
                  break
         else :
            print(num)


                  