'''built in class attributes of ' class '

1. __dict__ : it coontains class's namespace 
2.__doc__ : documentation string
3.__name__: class name given
4. __module: currrent working module
5.__bases__ : lsit of bases classes'''
class employee:
    '''this is employee class for maintianig employee data'''  # this line is a documentation string
    def __init__(self,father,mother,brother):
        self.father=father
        self.mother=mother
        self.brother=brother

f1 = employee('munegowda','nalakshmi','srinivas')

print(employee.__doc__) # if class is elsewhere and yoou need to know its function then doc helps
print(employee.__dict__)# it is the function that helps to print dictionary of varibles and there values
print(employee.__module__)  # module of the current class
print(employee.__name__)   # name of the current class 
print(employee.__bases__)