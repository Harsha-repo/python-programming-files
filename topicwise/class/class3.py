"""ways of organizing the python program 
 1. proceduarl oriented 
 2. functional oriented
 3. object oriented 
 1. it is line by line arrangement of codes 
 2. it is creating a function and write the program and helps to reuse the same code many times 
 3. it is creating an object and we can create as many copies of its function 
 it is process of creating the classes and objects 
 more focuses on data and logics 
 it provides iinheritence - reusablity
 encapsulation-data security 
 abstraction - data handling 
 
 class is a template or prtotype that helps to create objects 
 every objects belong to some class 
 techinically class is  a user defined data type
 some are classes that are in python 
 
 
 key word - class
 give a name to class ( identifier )
 inside give attributes and methods 
 
 then we make objects of that class 
 later we call to perform"""
class employee:
    def __init__(self):  # special method used for initializing objects with attributes
        self.name=input('enter your name:')
        self.age=int(input('enter your age:'))
        self.pro=input('enter your profession:')
    def show(self):
        print(self.name)
        print(self.age)
        print(self.pro)
    def family(self):
        self.x=input('enter yes or no whether having family or  not')
        if self.x=='no':
            breakpoint
        else:
            self.father=input('enter ur father name:')
            self.mother=input('enter your mother name:')
            self.brother=input('enter your brother name:')

"""types of constructers are there 
1. parametrized 
2.non parameterized 
3.default constructer 
__init__ is a non parameterized constructer which is above 


but if you pass the arguments to the constructers then that is called parameterized constructer 
hence we can give parameters values as input in objects 

if you write pass then it is default constructer """
            
        

e1=employee()
e1.show()
print(e1.__dict__) # this is a special fucntion that is used to form dictionary of the 
#elements that are initialized inside the constructer of the class 
# it is only particular for the constructer alone 




