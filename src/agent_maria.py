import random

class Agent_Maria():
    def __init__(self):
        pass
        #self.status_bce = BCE()

    #Evaluador general BCE,  salida solo un BCE
    def general_evaluator_bce(self,arr_bce):
        bce = random.choice(arr_bce)
        index = arr_bce.index(bce)  
        #print((bce, index),"Dato devuelto")                           
        return (bce, index)

    def comparator(self,bce_agente):
        arr_bce = [] 

        for i in range(7):
            arr_bce.append(bce_agente)
        
        return arr_bce