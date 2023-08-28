from sensory_nn import Sensory_NN
from bce import BCE
class Sensory_system():
    
    def __init__(self):
        
        self.list_senses = ["sight","hearing","smell","taste","touch","body","time"]
        self.senses = []
        for _, sense in enumerate(self.list_senses):
            self.senses.append(Sensory_NN(sense))
        

    def status(self):
        list_id_bce = []
        for index, _ in enumerate(self.list_senses):
            list_id_bce.append(self.senses[index].status())
        return list_id_bce

    def set_event(self,arr_event):
        list_id_bce=[]
        for index, _ in enumerate(self.list_senses):
            list_id_bce.append(self.senses[index].set_event(arr_event[index]))
        return list_id_bce
        
    def to_memory(self):
        list_return=[]
        for index, _ in enumerate(self.list_senses):
            list_return.append(self.senses[index].to_memory())     
        return list_return

    def update_neuron(self, arr_bce):
        list_id_bce=[]
        for index, _ in enumerate(self.list_senses):
            resultado = self.senses[index].update_neuron(arr_bce[index])
            if resultado is not None:
                list_id_bce.append(resultado)
        return list_id_bce
    
    def get_bce_from_mind(self,dictionary):
        list_return=[]
        bce_list = []
        index = ["biological","cultural","emotional"]
        for _, key in enumerate(self.list_senses):
            bce_list = []
            for key_bce in index:
                bce_list.append(dictionary[key][key_bce])
                #list_return.append(value)
            list_return.append(BCE(*bce_list))
        return list_return

    def init_patterns(self,arr_patternes_bce):
        list_return=[]
        for index, _ in enumerate(self.list_senses):
            list_return.append(self.senses[index].init_patterns(arr_patternes_bce[index]))
        return list_return
        
    def reset(self):
        for index, _ in enumerate(self.list_senses):
            self.senses[index].reset()
