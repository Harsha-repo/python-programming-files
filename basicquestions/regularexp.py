import re

pattern = r'91+\d{10}'
text = 'my number is 91+9731945055'

match = re.match(pattern,text)

# re.search for the first occurence of the pattern
# re.match checks the entire string 
# re.

