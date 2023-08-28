import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', 'src')
sys.path.append(src_dir)

from src.bce import BCE
import pytest
import random
from src.sensory_system import Sensory_system


def generar_lista_patrones(num_elementos,sense,letter):
    senses=["sight","hearing","smell","taste","touch","body","time"]
    arr_patterns_bce = []
    for i in range(num_elementos):
        nombre = f"pattern_{chr(ord(letter) + i)}_{sense}"
        patron = BCE().sample()
        arr_patterns_bce.append((nombre, patron))
    return arr_patterns_bce

def generar_lista_eventos(num_elementos,sense,letter):
    senses=["sight","hearing","smell","taste","touch","body","time"]
    arr_events_bce = []
    for i in range(num_elementos):
        nombre = f"{random.choice(arr_patterns_bce[senses.index(sense)])[0]}:event_{chr(ord(letter) + i)}_{sense}"
        patron = BCE().sample()
        arr_events_bce.append((nombre,patron))
    return arr_events_bce

def gen_arr_patterns_bce(num_items,letter):
    senses=["sight","hearing","smell","taste","touch","body","time"]
    arr_patterns_bce = []
    for sense in senses:
        arr_patterns_bce.append(generar_lista_patrones(num_items,sense,letter))
    return arr_patterns_bce

def gen_arr_events_bce(num_items,letter):
    senses=["sight","hearing","smell","taste","touch","body","time"]
    arr_patterns_bce = []
    for sense in senses:
        arr_patterns_bce.append(generar_lista_eventos(num_items,sense,letter))
    return arr_patterns_bce

senses=["sight","hearing","smell","taste","touch","body","time"]


arr_patterns_bce=gen_arr_patterns_bce(4,'a')

arr_patterns_bce2=gen_arr_patterns_bce(4,'e')

arr_events_bce=gen_arr_events_bce(4,'a')

arr_events_bce2=gen_arr_events_bce(4,'e')


def gen_expected_arr_patterns_bce(arr_patterns_bce,plus):
    expected_arr_patterns_bce=[]
    for item in arr_patterns_bce:
        tmp=[]
        for i, patterns in enumerate(item):
            tmp.append((i+plus,)+patterns)
        expected_arr_patterns_bce.append(tmp)
    return expected_arr_patterns_bce


expected_arr_patterns_bce=gen_expected_arr_patterns_bce(arr_patterns_bce,0)

expected_arr_patterns_bce2=gen_expected_arr_patterns_bce(arr_patterns_bce2,6)


events_bce_00 = [sensory_events[0] for sensory_events in arr_events_bce2]
events_bce_01 = [sensory_events[1] for sensory_events in arr_events_bce2]
events_bce_02 = [sensory_events[2] for sensory_events in arr_events_bce2]

event_00 = [tupla[0] for tupla in events_bce_00]
event_01 = [tupla[0] for tupla in events_bce_01]
event_02 = [tupla[0] for tupla in events_bce_02]

bce_00 = [tupla[1] for tupla in events_bce_00]
bce_01 = [tupla[1] for tupla in events_bce_01]
bce_02 = [tupla[1] for tupla in events_bce_02]


@pytest.fixture
def sensory_system():
    instance=Sensory_system()
    instance.init_patterns(arr_patterns_bce)
    instance.set_event(event_00)
    instance.update_neuron(bce_00)
    instance.set_event(event_01)
    instance.update_neuron(bce_01)

    return instance


@pytest.mark.parametrize("arr_pattern, expected", [
     (arr_patterns_bce, expected_arr_patterns_bce),
     (arr_patterns_bce2, expected_arr_patterns_bce2)
])
def test_init_patterns(sensory_system, arr_pattern, expected):
    result = sensory_system.init_patterns(arr_pattern)
    assert result == expected

# Generación de valores aleatorios para los patrones
num_patterns = 1000  # Número de patrones

senses=["sight","hearing","smell","taste","touch","body","time"]
# Generar casos de prueba para pytest.mark.parametrize

# Crear lista de patrones con valores BCE aleatorios

arr_patternes_7_senses = []
for sense in senses:
    arr_patternes_bce = []
    for i in range(num_patterns):
        pattern_name = f"{sense}_pattern_{i:02d}"
        bce_value = BCE().sample()
        arr_patternes_bce.append((pattern_name, bce_value, i))
    arr_patternes_7_senses.append(arr_patternes_bce)

# Lista de eventos aleatorios
event_list_7_senses=[]
for i, sense in enumerate(senses):
    #print(sense,i)
    events_list = [(f"{random.choice(arr_patternes_7_senses[i])[0]}:{sense}_event_{random.randint(0, 99):02d}",BCE().sample()) for _ in range(num_patterns//2)]
    events_list2 = [(f"{random.choice(arr_patternes_7_senses[i])[0]}:{random.choice(arr_patternes_7_senses[i])[0]}",BCE().sample()) for _ in range(num_patterns//2)]
    events_list+=events_list2
    event_list_7_senses.append(events_list)


num_test_cases = num_patterns

parameters_sensory_system_behavior = []

for i in range(num_test_cases):

    list_arr_sense=[]
    list_pattern_event=[]
    list_bce_event=[]
    list_output=[]
    
    for index_sense, sense in enumerate(senses):
        pattern = event_list_7_senses[index_sense][i][0].split(':')[0]
        event = event_list_7_senses[index_sense][i][0].split(':')[1]
        bce_pattern = next((data for p, data, _ in arr_patternes_7_senses[index_sense] if p == pattern ), None)
        bce_event = event_list_7_senses[index_sense][i][1]
        index = next((index for e, _, index in arr_patternes_7_senses[index_sense] if e == event), len(arr_patternes_7_senses[index_sense]))
        
        combined_info = [
            index,  # Índice del elemento seleccionado de pattern
            BCE.average(bce_event, bce_pattern) if index == len(arr_patternes_7_senses[index_sense]) else arr_patternes_7_senses[index_sense][index][1],
            pattern if index == len(arr_patternes_7_senses[index_sense]) else '',  # El pattern seleccionado
            event,       # El evento seleccionado
            sense
        ]
        pattern_event = f"{pattern}:{event}"
        output = combined_info
        arr_patternes_bce_2 = [(pattern, bce_value) for pattern, bce_value, _ in arr_patternes_7_senses[index_sense]]

        list_arr_sense.append(arr_patternes_bce_2)
        list_pattern_event.append(pattern_event)
        list_bce_event.append(bce_event)
        list_output.append(output)


    parameters_sensory_system_behavior.append((list_arr_sense,list_pattern_event,list_bce_event,list_output))



@pytest.mark.parametrize("arr_patterns_bce, pattern_events, bce_event, expected_output", parameters_sensory_system_behavior)
def test_sensory_system_behavior( arr_patterns_bce, pattern_events, bce_event, expected_output):
    sensory_system=Sensory_system()
    sensory_system.init_patterns(arr_patterns_bce)
    sensory_system.set_event(pattern_events)
    output = sensory_system.update_neuron(bce_event)

    assert output == expected_output