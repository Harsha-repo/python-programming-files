# given a string we have to remove the adjacent duplicates in the string 
# and also print the unique string 


s = 'abbaca'

stack = []

for char in s:
    if stack and char == stack[-1]:
        stack.pop()
    else:
        stack.append(char)
        
print(''.join(stack))



