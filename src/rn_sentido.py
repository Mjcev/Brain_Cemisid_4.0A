from neuronas import Neuronas


class RN_sentido():
    
    def __init__(self,sentido="vista"):
        self.neuronas = Neuronas()
        self.id = sentido

    def status(self):
        return self.neuronas.get_neuronas()

    def recibir_evento_bce(self,evento,bce):
        return [self.neuronas.recibir_evento_bce(evento,bce),self.id]

    def recibir_evento(self,evento):
        return [self.neuronas.recibir_evento(evento),self.id]

    def actualizar_neurona(self, bce):
        return [self.neuronas.actualizar_bce_neurona_por_aprender(bce),self.id]
    
    def init_patrones(self, arr_patrones_bce):
        self.neuronas.init_patrones(arr_patrones_bce)
