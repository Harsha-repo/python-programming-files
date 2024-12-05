class stationary:
    ownername='harsha'  # class variable
    def __init__(self,pen,pencil):
        self.pen=pen
        self.pencil=pencil
    @classmethod                 # inside this class method we can modify the class variable
                                  # and this is only for this block if insatances are printed 
                                  # we will get the modified  
    def newownername(cls):
        cls.ownername='seena'
        print(cls.ownername)
    
s1=stationary('brite','apsara')
s1.ownername
print(s1.ownername)  # the original class variable accessing 
s1.newownername()    # accessing the new modified class variable 
