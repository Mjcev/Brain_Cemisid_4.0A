from bce import BCE
import random

class Generator():

    def __init__(self):
        n_items=10
        pattern_arr=["pattern_zero","pattern_zero2"]+["pattern_{:03d}".format(i) for i in range(n_items)]
        self.generic_pattern_arr = [self.add_random_suffix(s) for s in pattern_arr]
        self.arr_senses=["sight","hearing","smell","taste","touch","body","time"]
        self.generic_event_arr=["event_{:03d}".format(i) for i in range(n_items)]
        self.arr_patternes_bce=[]

    def add_random_suffix(self,input_string):
        suffixes = ["_b", "_c", "_e"]
        random_suffix = random.choice(suffixes)
        string_with_suffix = input_string + random_suffix
        return string_with_suffix


    def gen_patterns(self):
        arr_patternes_bce=[]
        for sense in self.arr_senses:
            arr_senses = []
            for pattenr in self.generic_pattern_arr:
                if pattenr == "pattern_zero" or pattenr == "pattern_zero2" and sense != "time":
                    arr_senses.append([f"{sense}_{pattenr}",BCE().zero()])
                elif sense == "time":
                    arr_senses.append([f"{sense}_{pattenr}",BCE().time_sample()])
                else:
                    arr_senses.append([f"{sense}_{pattenr}",BCE().sample()])
            arr_patternes_bce.append(arr_senses)
        self.arr_patternes_bce=arr_patternes_bce
        return self.arr_patternes_bce

    def gen_event(self):
        #self.gen_patterns()
        sensory_event=[]
        for index, sense in enumerate(self.arr_senses):
            pattenr = random.choice(self.arr_patternes_bce[index])[0]
            event = random.choice(self.generic_event_arr)
            sensory_event.append(f"{pattenr}:{sense}_{event}")
        return sensory_event