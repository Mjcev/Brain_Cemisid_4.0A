from need import Need
#import numpy as np

class BCE():
    
    def __init__(self,need_bio=Need().sample(),need_cul=Need().sample(),need_emo=Need().sample(),size=len_degree):
        #action  6*3+1 =>19
        
        self.biologico = need_bio
        self.cultural = need_cul
        self.emocional = need_emo
    
    def state(self):
        return np.array([ self.biologico.state, self.cultural.state, self.emocional.state ], dtype=np.int_)  
        
        #self.sign_str={0:"+",1:"-"}
    def __str__(self):
        return f"Biologico:{str(self.biologico)} Cultural:{str(self.cultural)} Emocional:{str(self.emocional)}"

    def __repr__(self):
        return f"Biologico:{str(self.biologico)} Cultural:{str(self.cultural)} Emocional:{str(self.emocional)}"
    
    def __add__(self, other):
        return BCE(self.biologico+other.biologico,self.cultural+other.cultural,self.emocional+other.emocional)
    
    def __sub__(self, other):
        return BCE(self.biologico-other.biologico,self.cultural-other.cultural,self.emocional-other.emocional)
    
    def __mul__(self, escalar):
        return BCE(self.biologico*escalar,self.cultural*escalar,self.emocional*escalar)
    
    def __floordiv__(self, escalar):
        return BCE(self.biologico//escalar,self.cultural//escalar,self.emocional//escalar)
    
    def __truediv__(self, escalar):
        return BCE(self.biologico/escalar,self.cultural/escalar,self.emocional/escalar)
    
    def reset(self):
        self.biologico.reset()
        self.cultural.reset()
        self.emocional.reset()



    def sample(self):
        return BCE(self.biologico.sample(),self.cultural.sample(),self.emocional.sample())
    
    def time_sample(self):
        return BCE(self.biologico.time_sample(),self.cultural.time_sample(),self.emocional.time_sample())
    
    def zero(self):
        return BCE(Need().zero(), Need().zero(), Need().zero())
    
    def none(self):
        return BCE(Need().none(), Need().none(), Need().none())
