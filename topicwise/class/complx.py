class complex:
    def complexnumber(self):
        self.real=int(input('enter the real value of complex:'))
        self.img=int(input('enter your img naumber of complex:'))
    def display(self):
        print(self.real,'+','i',self.img,sep="")
    def sum(self,c1,c2):
        self.real=c1.real+c2.real
        self.img=c1.img+c2.img
c1=complex()
c1.complexnumber()
c2=complex()
c2.complexnumber()
c1.display()
c2.display()
c3=complex()
c3.sum(c1,c2)
c3.display()

                       
c1.img=5

print(c1.__dict__)
c3.sum(c1,c2)
c3.display()
print(c1.real)