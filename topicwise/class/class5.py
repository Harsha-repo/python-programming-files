"""accessing the class memebers """
class employee:
    def __init__(self):
        self.salary=3000
        self.age=21
        self.name='h'

    def show(self):
        print('salary is ',self.salary)
e1=employee()
e2=employee()
e1.show()   # . is to acess the methods inside the class now it gives the output accordingly
print(e1.__dict__)

