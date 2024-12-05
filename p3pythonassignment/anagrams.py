# NAME : HARSHA M
# USN  : 1CR22AI044

# Anagrams

s1 = 'silent'
s2 = 'listen'

str1 = s1.lower()
str2 = s2.lower()

if sorted(str1)==sorted(str2):
    print('anagram')
else:
    print('not anagram')