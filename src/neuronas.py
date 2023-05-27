from bce import BCE

class Neuronas():
    def __init__(self):
        self.neuronas_aprendidas = {}
        self.neurona_por_aprender = {}

        self.tmp = None

    def recibir_evento(self, string):
        patron, evento = string.split(":")
        
        if evento not in self.neuronas_aprendidas:
            self.neurona_por_aprender[evento]=[len(self.neuronas_aprendidas),self.neuronas_aprendidas[patron][1]]
            return self.neurona_por_aprender[evento]
        else:
            self.tmp = self.neuronas_aprendidas[evento]
            return self.neuronas_aprendidas[evento]
        
    def recibir_evento_bce(self, evento, bce):
        if evento not in self.neuronas_aprendidas:
            self.neurona_por_aprender[evento]=[len(self.neuronas_aprendidas),BCE().none()]
            self.actualizar_bce_neurona_por_aprender(bce)

        return self.neuronas_aprendidas[evento]

    def actualizar_bce_neurona_por_aprender(self, bce):
        if bool(self.neurona_por_aprender):
            evento, value = self.neurona_por_aprender.popitem()
            id_neurona = len(self.neuronas_aprendidas)
            self.neuronas_aprendidas[evento]=[id_neurona,(bce+value[1])//2]
            return self.neuronas_aprendidas[evento]
        else:
            return self.tmp 

    def init_patrones(self,arr_patrones_bce):
        for patron_bce in arr_patrones_bce:
            self.neuronas_aprendidas[patron_bce[0]]=[len(self.neuronas_aprendidas),patron_bce[1]]

    def get_neuronas(self):
        return self.neuronas_aprendidas

