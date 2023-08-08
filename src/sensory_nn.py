from neurons import Neurons


class Sensory_NN():
    
    def __init__(self,sense="sight"):
        self.neurons = Neurons()
        self.id = sense

    def status(self):
        return self.neurons.get_neurons()

    def set_event_bce(self,event,bce):
        if not event.endswith("_sight"):
            event += self.id,bce

        return [self.neurons.set_event_bce(event,bce),self.id]

    def set_event(self,event):
        
        pattern_event = event.split(':')[0] +":" + event.split(':')[1] +"_"+self.id
        return [self.neurons.set_event(pattern_event),self.id]

    def update_neuron(self, bce):
        return [self.neurons.update_neuron_to_learn(bce),self.id]
    
    def init_patterns(self, arr_patterns_bce):
        result_list = [(pattern + "_" + self.id, bce) for pattern, bce in arr_patterns_bce]
        #print(result_list)
        return self.neurons.init_patterns(result_list)
        

    def reset(self):
        self.neurons.reset()
        