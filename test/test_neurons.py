import os
import sys
import random
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', 'src')
sys.path.append(src_dir)

from src.bce import BCE
import pytest
from src.neurons import Neurons


a=BCE().sample()
b=BCE().sample()
c=BCE().sample()
d=BCE().sample()
event0=BCE().sample()
event1=BCE().sample()
event2=BCE().sample()
event3=BCE().sample()
event4=BCE().sample()

arr_patternes_bce=[("pattern_a",a),("pattern_b",b),("pattern_c",c),("pattern_d",d)]
arr_patternes_bce2=[("pattern_e",a),("pattern_f",b),("pattern_g",c),("pattern_h",d)]


@pytest.fixture
def neurons():
    instance=Neurons()
    arr_patternes_bce=[("pattern_a",a),("pattern_b",b),("pattern_c",c),("pattern_d",d)]
    instance.init_patterns(arr_patternes_bce)
    instance.set_event("pattern_a:event0")
    instance.update_neuron_to_learn(event0)
    instance.set_event("pattern_b:event1")
    instance.update_neuron_to_learn(event1)
    instance.set_event("pattern_c:event2")
    instance.update_neuron_to_learn(event2)
    return instance



@pytest.mark.parametrize("arr_pattern, expected", [
    ( arr_patternes_bce2, [(7,"pattern_e",a),(8,"pattern_f",b),(9,"pattern_g",c),(10,"pattern_h",d)]),
    ( arr_patternes_bce, [(0,"pattern_a",a),(1,"pattern_b",b),(2,"pattern_c",c),(3,"pattern_d",d)]),
])
def test_init_patterns(neurons, arr_pattern, expected):
    result = neurons.init_patterns(arr_pattern)
    assert result == expected


@pytest.mark.parametrize("event, bce_value, expected", [
    ("pattern_x", a, [7, a,"","pattern_x"]),
    ("pattern_y", b, [7, b,"","pattern_y"]),
    ("pattern_z", c, [7, c,"","pattern_z"])
])
def test_set_event_bce(neurons, event, bce_value, expected):
    result = neurons.set_event_bce(event, bce_value)
    assert result == expected


@pytest.mark.parametrize("input_string, expected", [
    ("pattern_a:pattern_a", [0,a,"","pattern_a"]),
    ("pattern_b:event1", [5, BCE.average(event1,b),"pattern_b","event1"]),
    ("pattern_c:event2", [6, BCE.average(event2,c),"pattern_c","event2"]),
    ("pattern_c:event3", [7, c,"pattern_c","event3"]),
    ("event0:event4", [7, BCE.average(event0,a),"event0","event4"]),
])
    
def test_set_event(neurons,input_string, expected):
    result = neurons.set_event(input_string)
    assert result == expected
    


@pytest.mark.parametrize("input_string, bce_value, expected", [
    ("pattern_a:pattern_a", a, [0,a,"","pattern_a"]),
    ("pattern_b:event1", event1, [5, BCE.average(event1,b),"pattern_b","event1"]),
    ("pattern_c:event2", event2, [6, BCE.average(event2,c),"pattern_c","event2"]),
    ("pattern_c:event3", event3, [7, BCE.average(event3,c),"pattern_c","event3"]),
    ("event0:event4", event4, [7, BCE.average(event4,BCE.average(event0,a)),"event0","event4"]),
    ("pattern_a:event6", event3, [7, BCE.average(event3,a),"pattern_a","event6"]),
])
def test_update_neuron_to_learn(neurons, input_string, bce_value, expected):
    neurons.set_event(input_string)
    result = neurons.update_neuron_to_learn(bce_value)
    assert result == expected

@pytest.mark.parametrize("arr_pattern, expected", [
    ( arr_patternes_bce, {
        'pattern_a': [0, a,"","pattern_a"],
        'pattern_b': [1, b,"","pattern_b"],
        'pattern_c': [2, c,"","pattern_c"],
        'pattern_d': [3, d,"","pattern_d"],
        'event0': [4, BCE.average(event0,a),"pattern_a","event0"],
        'event1': [5, BCE.average(event1,b),"pattern_b","event1"],
        'event2': [6, BCE.average(event2,c),"pattern_c","event2"]
        }),
    ( arr_patternes_bce2, {
        'pattern_a': [0, a,"","pattern_a"],
        'pattern_b': [1, b,"","pattern_b"],
        'pattern_c': [2, c,"","pattern_c"],
        'pattern_d': [3, d,"","pattern_d"],
        'event0': [4, BCE.average(event0,a),"pattern_a","event0"],
        'event1': [5, BCE.average(event1,b),"pattern_b","event1"],
        'event2': [6, BCE.average(event2,c),"pattern_c","event2"],
        "pattern_e" : [7,a,"","pattern_e"],
        "pattern_f" : [8,b,"","pattern_f"],
        "pattern_g" : [9,c,"","pattern_g"],
        "pattern_h" : [10,d,"","pattern_h"]
        }),
    
])

def test_get_neurons(neurons, arr_pattern, expected):
    neurons.init_patterns(arr_pattern)
    result = neurons.get_neurons()
    assert result == expected

def test_reset(neurons):
    neurons.reset()
    assert neurons.learned_neurons == {}
    assert neurons.neuron_to_learn == {}

# Generación de valores aleatorios para los patrones
num_patterns = 1000  # Número de patrones
# Generar casos de prueba para pytest.mark.parametrize
parameters_neurons_behavior = []
# Crear lista de patrones con valores BCE aleatorios
arr_patternes_bce = []
for i in range(num_patterns):
    pattern_name = f"pattern_{i:02d}"
    bce_value = BCE().sample()
    arr_patternes_bce.append((pattern_name, bce_value, i))

# Lista de eventos aleatorios

events_list = [(f"{random.choice(arr_patternes_bce)[0]}:event_{random.randint(0, 99):02d}",BCE().sample()) for _ in range(num_patterns//2)]
events_list2 = [(f"{random.choice(arr_patternes_bce)[0]}:{random.choice(arr_patternes_bce)[0]}",BCE().sample()) for _ in range(num_patterns//2)]
events_list+=events_list2


num_test_cases = num_patterns
for i in range(num_test_cases):
    pattern = events_list[i][0].split(':')[0]
    event = events_list[i][0].split(':')[1]
    bce_pattern = next((data for p, data, _ in arr_patternes_bce if p == pattern ), None)
    bce_event = events_list[i][1]
    index = next((index for e, _, index in arr_patternes_bce if e == event), len(arr_patternes_bce))
    combined_info = [
        index,  # Índice del elemento seleccionado de pattern
        BCE.average(bce_event, bce_pattern) if index == len(arr_patternes_bce) else arr_patternes_bce[index][1],
        pattern if index == len(arr_patternes_bce) else '',  # El pattern seleccionado
        event       # El evento seleccionado
    ]
    pattern_event = f"{pattern}:{event}"
    output = combined_info
    parameters_neurons_behavior.append((arr_patternes_bce, pattern_event, bce_event, output))


@pytest.mark.parametrize("arr_patterns_bce, pattern_events, bce_event, expected_output",parameters_neurons_behavior)
def test_neurons_behavior(arr_patterns_bce, pattern_events, bce_event, expected_output):
    neurons=Neurons()
    neurons.init_patterns(arr_patterns_bce)

    neurons.set_event(pattern_events)
    output = neurons.update_neuron_to_learn(bce_event)
    
    assert output == expected_output