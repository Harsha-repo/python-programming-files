import sys 
print(sys.getrecursionlimit())   
 # setting the limit of the recursion value to needed limit 
sys.setrecursionlimit(200) 
print(sys.getrecursionlimit())    # using get recursion method know the limit set by user 
def demo():
    
    
    demo()
#demo()
''' advantages are 
11.clean code
2. complex problems are solved 
diadvantges 
hard to debug that is hard to understand the flow of programme 
not memory efficint '''