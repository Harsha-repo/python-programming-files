# You are given an expression string, write a program to examine whether the pairs 
# and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression using a function. 
# The function will return True
# if the expression is balanced and print Balanced. The function will return False if the expression is 
# not balanced and print Not Balanced


s = ' {[()()]}'

stack = []
matches = {')':'(' , ']':'['  , '}':'{'}
for char in s:
    if char in '({[':
        stack.append(char)
    elif char in ')}]':
        if not stack and stack[-1]!=stack[char]:
            print('no')
        else:
            stack.pop()
if not stack:
    print('yes')
else:
    print('no')