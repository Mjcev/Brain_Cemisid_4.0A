import random
import numpy as np

LEN_DEGREE=4

class Need():
    def __init__(self, sign=0, degree=0, len_degree=LEN_DEGREE):

        self.len_sign=2
        self.len_degree=len_degree
        
        if sign==None and degree==None:
            self.state = np.array([sign,degree]) 
        else:
            self.state = np.array([sign,degree], dtype=np.int_) 
        
        self.sign_str={0:"+",1:"-"}

    def __str__(self):
        if self.state[0]!=None and self.state[1]!=None:
            return f"{self.sign_str[self.state[0]]}{self.state[1]/self.len_degree}"
        else:
            return "None"
    
    def __repr__(self):
        if self.state[0]!=None and self.state[1]!=None:
            return f"{self.sign_str[self.state[0]]}{self.state[1]/self.len_degree}"
        else:
            return "None"
        
    
    def __add__(self, other):
        if other.state[0]==None or other.state[1]==None:
            return Need(self.state[0],self.state[1])
        elif self.state[0]==None or self.state[1]==None:
            return Need(other.state[0],other.state[1])

        if self.state[1] == 0 and other.state[1] == 0:
            return Need(self.state[0],self.state[1])
        
        elif self.state[0]==0:
            if other.state[0] == 0:
                sign = 0
                degree = self.state[1]+other.state[1]
            else:
                if self.state[1] >= other.state[1]:
                    sign = 0
                    degree = self.state[1]-other.state[1]
                else:
                    sign = 1
                    degree = abs(self.state[1]-other.state[1])
        else:
            if other.state[0] == 1:
                sign = 1
                degree = self.state[1]+other.state[1]
            else:
                if self.state[1] >= other.state[1]:
                    sign = 1
                    degree = self.state[1]-other.state[1]
                else:
                    sign = 0
                    degree = abs(self.state[1]-other.state[1])
                    
        return Need(sign,min(degree,self.len_degree))
    
    def __sub__(self, other):	#To get called on subtraction operation using - operator.  
        if other.state[0] == None and other.state[1] == None:
            return self
        elif other.state[0] == 0:
            sign=1
        elif other.state[0] == 1:
            sign=0
        return self+Need(sign,other.state[1])

    def __mul__(self, scalar):	#To get called on multiplication operation using * operator.
        if self.state[0] == 0 and scalar >= 0:
            sign=0
        elif self.state[0] == 1 and scalar < 0:
            sign=0
        else:
            sign=1
        return Need(sign,self.state[1]*abs(scalar))+Need(0,0)

    def __truediv__(self, scalar):	#To get called on division operation using / operator.
        if self.state[0] == 0 and scalar >= 0:
            sign=0
        elif self.state[0] == 1 and scalar < 0:
            sign=0
        else:
            sign=1
        return Need(sign,self.state[1]/abs(scalar))+Need(0,0)

    def __floordiv__(self, scalar):	#To get called on division operation using // operator.
        if self.state[0] == 0 and scalar >= 0:
            sign=0
        elif self.state[0] == 1 and scalar < 0:
            sign=0
        else:
            sign=1
        return Need(sign,self.state[1]//abs(scalar))+Need(0,0)

    def __lt__(self, other):    #To get called on comparison using < operator.
        if self.state[0]==None and self.state[1]==None and other.state[0]!=None and other.state[1]!=None:
            return True
        elif other.state[0]==None and other.state[1]==None and self.state[0]!=None and self.state[1]!=None:
            return False
        elif self.state[0]==0 and other.state[0]==0:
            return self.state[1] < other.state[1]
        elif self.state[0]==1 and other.state[0]==1:
            return self.state[1] > other.state[1]
        elif self.state[0]==0 and other.state[0]==1:
            return False
        elif self.state[0]==1 and other.state[0]==0:
            return True
        
    def __eq__(self, other):    #To get called on comparison using == operator.
        if self.state[0]==other.state[0] and self.state[1]==other.state[1]:
            return True
        else:
            return False

    def __ne__(self, other):    #To get called on comparison using != operator.
        if self == other:
            return False

    def __le__(self, other):    #To get called on comparison using <= operator.
        if self == other:
            return True
        elif self < other:
            return True
        else:
            return False

    def __gt__(self, other):    #To get called on comparison using > operator.
        if self < other:
            return False
        else:
            return True

    def __ge__(self, other):    #To get called on comparison using >= operator.
        if self == other:
            return True
        elif self > other:
            return True
        else:
            return False

    def reset(self):
        sign=random.randint(0,self.len_sign-1)
        degree=random.randint(0,self.len_degree-1)
        self.state=np.array([sign,degree], dtype=np.int_)
        return self

    def sample(self):
        sign=random.randint(0,self.len_sign-1)
        degree=random.randint(0,self.len_degree-1)
        return Need(sign,degree)

    def time_sample(self):
        sign=1
        degree=random.randint(0,self.len_degree-1)
        return Need(sign,degree)

    def zero(self):
        sign=0
        degree=0
        self.state=np.array([sign,degree], dtype=np.int_)
        return self

    def none(self):
        sign=None
        degree=None
        self.state=[sign,degree]
        return self

    def average(self, other):
        if self.state[0]==0:
            item1=self.state[1]
        else:
            item1=self.state[1]*(-1)

        if other.state[0]==0:
            item2=other.state[1]
        else:
            item2=other.state[1]*(-1)

        avg=(item1+item2)//2

        if avg<0:
            return Need(1,abs(avg))+Need(0,0)
        else:
            return Need(0,abs(avg))+Need(1,0)

