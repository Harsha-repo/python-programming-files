#NAME : HARSHA M
#USN  : 1CR22AI044

# 1. VALID PHONE NUMBER

# Python program to check if 
# given mobile number is valid
# 1) Begins with 0 or 91
	# 2) Then contains 6,7 or 8 or 9.
	# 3) Then contains 9 digits

import re

def isValid(s):
	
	
	Pattern = re.compile("(0|91)?[6-9][0-9]{9}")    
	return Pattern.match(s)


s = "347873923408"

if (isValid(s)): 
	print ("Valid Number")	 
else :
	print ("Invalid Number") 


