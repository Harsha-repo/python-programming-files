'''priinting the reverse order number from n to 1'''

def reversenum(n):   # initializing the function
    if n==0:     # we set tehe limit and then try to stop recursioon the this limit
        return    # like wise in loops we use break here its return , as soon as the limit is rached it return nohting 
                # then recursion stops 
    print(n)      # if n >0 then it prints n value to each iteration 
    return reversenum(n-1) # this will return the value of n making it n-1

reversenum(10)

''' syntax for recursion 
def func():
    base conditon:
      return 
    code
    return(recursive calls )'''
""" if a functtion calls another function and that function calls the first function then it is called 
indirect recursion 
"""

def function1(x):
    if x<=0:
        return
    print(x,end='')
    function2(x-1)
def function2(x):
    if x==0:
        return
    print(x,end='')
    function1(x-1)
function1(20)