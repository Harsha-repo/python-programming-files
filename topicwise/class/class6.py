""" buitinfunctions of the class 
1. getattr(object_name,attribute_name)      # important is attribute names and values should be in the string form
2.setattr(object_name,attributename,new_value)
3.delattr(object_name,atribute_name)
4.hasattr(object_name,attribute_name)""" # this checks whether the attribute that is entered by me is present or not in the class
# the out put is in the form of boolean True or false 

class employee:
    def __init__(self,father,mother,brother):
        self.father=father
        self.mother=mother
        self.brother=brother

f1 = employee('munegowda','nalakshmi','srinivas')

print(f1.__dict__)
setattr(f1,'mother','nagalakshmi')
print(f1.mother)
print(f1.__dict__)
delattr(f1,'brother')
print(f1.__dict__)
print(getattr(f1,'mother')) # in this place if i give brother it pops error because in the above code brother got deleted hence
print(hasattr(f1,'brother' ))                         

# in this way the attributes are used conviniently
# in the above example all the attributes are being examined 