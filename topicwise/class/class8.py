'''creating the instance variables 
1. using constructer
2. using instance method
3. outside the class'''

class student:
    def __init__(self,name,marks): # this is using the constructer we usually do 
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name,self.marks)    

s1=student('harhsa',88)
s2=student('srinivas',89)
s3=student('hari',89)
print(s1.__dict__)
print(s1.marks)
print(s3.name)
print(s3.__dict__)
#creating the new variable instances outside the class
s1.age=20
# now if i print the dict of student 1  there is new paremeter that is added 
print(s1.__dict__)  # s it works 
''' with this we can create the variables to a particular class object where you need to add a 
new parameter '''

# calling the isntance method that is defined inside the class the print the details 
s1.display()
 

''' here iam creating an method or function that is helping me to display the 
 results what i wanted 
  if  i want to print the student 2 details the i would call it with s2 object a below  '''
s2.display()
