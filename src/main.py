from rn_7_sentidos import RN_7_sentidos
from agente_inteligente import Agente_Inteligente

rn_sentidos = RN_7_sentidos()
agente_inteligente = Agente_Inteligente()

#Agente Daniel
memoria_daniel = MemoriaDaniel()

#Lista de eventos de entradas
eventos = []

#entrada de eventos a la red neuronal de michael
bce_7 = rn_sentidos.recibir_evento(eventos) #-> (BCE, #RN, evento):

#entrada del comparador 1 de maria para actualizar los bce de las neuronas
agente_inteligente.actualizar_neurona(AgenteMaria().comparador)

#Datos de las neuronas actualizadas con sus bce
bce_7_actualizado = agente_inteligente.status()

#Entrada de ids de las neuronas al modulo de memoria de daniel
memoria_daniel.set_rn(bce_7_actualizado.id)

#Agente Maria que requiere como entrada la memoria de daniel
mind = Mind(memoria_daniel)

#Agente de Maria que requiere como entrada los BCE en formato de diccionario y 
mind.start_process(bce_7.traduccion,  agente_inteligente.status())

