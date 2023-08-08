#from sensory_system import Sensory_system
#from intelligent_agent import Intelligent_agent
#
#sensory_system = Sensory_system()
#intelligent_agent = Intelligent_agent()
#
##Agente Daniel
#memoria_daniel = MemoriaDaniel()
#
##Lista de eventos de entradas
#eventos = []
#
##entrada de eventos a la red neuronal de michael
#bce_7 = sensory_system.set_event(eventos) #-> (BCE, #RN, evento):
#
##entrada del comparador 1 de maria para actualizar los bce de las neuronas
#sensory_system.update_neuron(AgenteMaria().comparador)
#
##Datos de las neuronas actualizadas con sus bce
#bce_7_actualizado = agente_inteligente.status()
#
##Entrada de ids de las neuronas al modulo de memoria de daniel
#memoria_daniel.set_rn(bce_7_actualizado.id)
#
##Agente Maria que requiere como entrada la memoria de daniel
#mind = Mind(memoria_daniel)
#
##Agente de Maria que requiere como entrada los BCE en formato de diccionario y 
#mind.start_process(bce_7.traduccion,  agente_inteligente.status())
#
