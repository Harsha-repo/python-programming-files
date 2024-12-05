# input things from the user weight , type , price  as per chicken weight 
todaypriceofsmall=100
todaypriceofbig = 120

weight = float(input('Enter the weight of chicken: '))
print(' FOR BIG BOILER PRESS :  1  ,  FOR SMALL BOILER PRESS : 2 ')

type = input()

if type=='1':
    print('BIG BOILER :',weight,'KG')
    print('TOTAL AMOUNT : RS',weight*todaypriceofbig)
    

elif type =='2':
    print('SMALL BOILER :', weight,'KG')
    print('TOTAL AMOUNT : RS',weight*todaypriceofsmall)

else:
    print('check the above statement correctly')




# when i saw a chicken shop owner entering the weight and type of chicken using his billing machine got an 
# idea of creating its prototype here it is 