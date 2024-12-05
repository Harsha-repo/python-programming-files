''' class vriables are the variables that are created entire class 
only one class variable copy is created for all the objects 
below the class it is created  and is used for the entire objects 
 '''

class student():
    grace = 10   # this is the class varible that can be used to all the objects of the class 
    def __init__(self):
        self.name=input('enter the student name:')
        self.marks=int(input('enter student marks :'))
    def result(self):
        print('student name is :',self.name)
        print('obtained marks is :',self.marks)
        print('the previous  result is :',self.marks)
        print('the result after adding grace is ',self.marks+self.grace)

s1=student()
student.grace  # accessing the classs variable using class name 
s1.grace       # using class object  
print('******grace marks is ',student.grace,'*********')
s1.result()
s2 = student()
s2.result()
'''' if u try to change the class variable value then it will create a new variable and 
do not change the real one '''
s2.grace=15
print(s2.__dict__)

''' class method 
* method which works on class variable 
*  first argument is class reference 

like we see that self is used to refer insatance variable 
for class variable we us cls
* made using decorator '@classmethod' '''# it is a built in function 






