year = int(input("enter the year:"))

if year%100==0 and year%400==0 :
    print('is leap  year')

elif year%100!=0 and year%4==0  :
    print('is leap year')
else:
    print('not a leap  year')