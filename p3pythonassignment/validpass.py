#NAME : HARSHA M
#USN : 1CR22AI044

# 2. VALID PASSWORD

# Password validation in Python
# using naive method

p = input("enter the password:")

spchar = ['$', '@', '#', '%']
val = True
#coditions for a valid passoword

if len(p)<6:
	print('length of password should be greater then 6 characters')
	val=False
if len(p)>20:
	print('the length of the password should be less then 20')
	val=False
if not any(char.isdigit()  for char in p):
	print('password should atleast contain a number')
	val = False
if not any(char.isupper() for char in p):
	print('password should contain atleast one upper case')
if not any(char in spchar for char in p):
	print('password should have atleast one special symbol')
	


if val:
	print('valid password')
else:
	print('invalid password')