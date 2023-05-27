from bce import BCE

class Agente_Inteligente():
    
    def __init__(self):
        self.estado_bce = BCE().zero()

    def status(self):
        return self.estado_bce

    def add_bce(self,bce):
        self.estado_bce += bce
        return self.estado_bce
    
    def __str__(self) -> str:
        return str(self.estado_bce)
    
    def __repr__(self) -> str:
        return str(self.estado_bce)