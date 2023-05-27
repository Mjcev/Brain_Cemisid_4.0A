from bce import BCE
import random

class Generador():

    def __init__(self):
        self.arr_patron_generico=["patron_zero","patron_a","patron_b","patron_c","patron_d","patron_e","patron_f","patron_g","patron_zero2"]
        self.arr_sentidos=["vista","oido","olfato","gusto","tacto","cuerpo","tiempo"]
        self.arr_eventos_genericos=["evento_a","evento_b","evento_c","evento_d","evento_e","evento_f","evento_g","evento_h","evento_i"]
        self.arr_patrones_bce=[]

    def crear_patrones(self):
        arr_patrones_bce=[]
        for sentido in self.arr_sentidos:
            arr_sentidos = []
            for patron in self.arr_patron_generico:
                if patron == "patron_zero" or patron == "patron_zero2" and sentido != "tiempo":
                    arr_sentidos.append([f"{patron}_{sentido}",BCE().zero()])
                elif sentido == "tiempo":
                    arr_sentidos.append([f"{patron}_{sentido}",BCE().time_sample()])
                else:
                    arr_sentidos.append([f"{patron}_{sentido}",BCE().sample()])
            arr_patrones_bce.append(arr_sentidos)
        self.arr_patrones_bce=arr_patrones_bce
        return self.arr_patrones_bce

    def crear_eventos_sensoriales(self):
        #self.crear_patrones()
        evento_sensorial=[]
        for index, sentido in enumerate(self.arr_sentidos):
            patron = random.choice(self.arr_patrones_bce[index])[0]
            evento = random.choice(self.arr_eventos_genericos)
            evento_sensorial.append(f"{patron}:{evento}")
        return evento_sensorial

    #crear_eventos_sensoriales(arr_sentidos,arr_eventos,patrones_init)


#patrones_init
