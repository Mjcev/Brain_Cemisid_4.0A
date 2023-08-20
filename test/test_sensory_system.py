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