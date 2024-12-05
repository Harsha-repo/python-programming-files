import random
aibatting=[]
userbatting =[]
aitoss = random.randint(1-6)

print("odd or eve  if odd press 1 if eve press 2")
odd = 1
eve=2
print('enter odd or eve')
usertoss = int(input('enter odd or eve'))

if(aitoss%2==0):
    ai = random.ranint(1-2)
    print('ai won the toss ')
    if ai==1:
        print('ai choose to bat')
        while(True):
            userbatting.append(int(input("user bowling value :")))
            aibatting.append(random.randint(1,6))
            print('computer batting value:',)
            
            
    else:
        print('ai choose to bowl')

    








#if computer wins it should pick bat or bowl randomly 
# if user wins users picks the bat or bowl manually 
# 