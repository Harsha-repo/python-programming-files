# in a string is ( this then check for ) this for all the brackets present in the string
# and also enure that all opening brackets have the closing brackets

s = '(())'

stack = []

for char in s:
    if char =='(':
        stack.append(char)
    if char ==')':
        if not stack:
            print( 'NO')
        
        stack.pop()
        
if not stack:
    print('yes')
else:
    print('NO')