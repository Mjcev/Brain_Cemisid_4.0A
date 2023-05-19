from rn_sentido import RN_sentido

class RN_7_sentidos():
    
    def __init__(self):
        
        self.list_sentidos = ["vista","oido","olfato","gusto","tacto","cuerpo","tiempo"]
        self.sentidos = []
        for _, sentido in enumerate(self.list_sentidos):
            self.sentidos.append(RN_sentido(sentido))
        

    def status(self):
        list_id_bce = []
        for index, sentido in enumerate(self.list_sentidos):
            list_id_bce.append(self.sentidos[index].status())
        return list_id_bce

    def recibir_evento(self,arr_evento):
        list_id_bce=[]
        for index, sentido in enumerate(self.list_sentidos):
            list_id_bce.append(self.sentidos[index].recibir_evento(arr_evento[index]))
        return list_id_bce
        

    def actualizar_neurona(self, arr_bce):
        list_id_bce=[]
        for index, sentido in enumerate(self.list_sentidos):
            resultado = self.sentidos[index].actualizar_neurona(arr_bce[index])
            if resultado is not None:
                list_id_bce.append(resultado)
        return list_id_bce
    
    
    def init_patrones(self,arr_patrones_bce):
        for index, sentido in enumerate(self.list_sentidos):
            self.sentidos[index].init_patrones(arr_patrones_bce[index])
        

