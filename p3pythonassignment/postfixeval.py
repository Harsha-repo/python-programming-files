e = ' 2 3 1 * + 9 -'
stack=[]
result = 0
exp = e.split()
for char in exp:
    if char.isdigit():
        stack.append(int(char))
    else:
        op1 = stack.pop()
        op2 = stack.pop()
        
    if char =='+':
        result = op1+op2
        
    if char =='-':
        result = op1-op2
    if char == '*':
        result = op1*op2
    if char == '/':
        result = op1/op2
    stack.append(result)
    
print(stack.pop())
        
