n = int(input('enter number of students:'))
i=0
while i<n:

    class student:
       def __init__(self):
          self.name = input('enter your name :')
          self.usn = int(input('enter your usn:'))

    def marks(self):
        self.marks=[]
        self.marks.append(int(input('enter your physics marks:')))
        self.marks.append(int(input('enter your math marks:')))
        self.marks .append(int(input('enter your chemistry marks:')))
    def result(self):
        print('*******result*******')
        print('physics =',self.marks[0])
        print('maths =',self.marks[1])
        print('chemsity=',self.marks[2])
        
        print('TOTAL = ',(self.marks[0]+self.marks[1]+self.marks[1]))
        print('percentage = ',((self.marks[0]+self.marks[1]+self.marks[1])/300)*100)

s1 = student()
s1.marks()
s1.result()
i=i+1
