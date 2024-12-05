try:
    n=int(input('enter an integer :'))
    assert n>=0,'pls enter an integer other than zero'
    print('the entered numbre is :',n)

except AssertionError:
    print('enter a positive  digit ')
    