import os
import sys

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
event=BCE().sample()
event1=BCE().sample()
event2=BCE().sample()
event3=BCE().sample()
arr_patternes_bce=[("pattern_a",a),("pattern_b",b),("pattern_c",c),("pattern_d",d)]
arr_patternes_bce2=[("pattern_e",a),("pattern_f",b),("pattern_g",c),("pattern_h",d)]


@pytest.fixture
def neurons():
    instance=Neurons()
    arr_patternes_bce=[("pattern_a",a),("pattern_b",b),("pattern_c",c),("pattern_d",d)]
    instance.init_patterns(arr_patternes_bce)
    instance.set_event("pattern_a:event0")
    instance.update_neuron_to_learn(event)
    instance.set_event("pattern_b:event1")
    instance.update_neuron_to_learn(event1)
    instance.set_event("pattern_c:event3")
    instance.update_neuron_to_learn(event3)
    return instance



@pytest.mark.parametrize("arr_pattern, expected", [
    ( arr_patternes_bce2, [(7,"pattern_e",a),(8,"pattern_f",b),(9,"pattern_g",c),(10,"pattern_h",d)]),
    ( arr_patternes_bce, [(0,"pattern_a",a),(1,"pattern_b",b),(2,"pattern_c",c),(3,"pattern_d",d)]),
])
def test_init_patterns(neurons, arr_pattern, expected):
    result = neurons.init_patterns(arr_pattern)
    assert result == expected


@pytest.mark.parametrize("event, bce_value, expected", [
    ("pattern_x", a, [7, a]),
    ("pattern_y", b, [7, b]),
    ("pattern_z", c, [7, c])
])
def test_set_event_bce(neurons, event, bce_value, expected):
    result = neurons.set_event_bce(event, bce_value)
    assert result == expected


@pytest.mark.parametrize("input_string, expected", [
    ("pattern_a:pattern_a", [0,a]),
    ("pattern_b:event1", [5, event1.average(b)]),
    ("pattern_c:event2", [7, c]),
    ("pattern_c:event5", [7, c]),
    ("event0:event3", [6, event3.average(c)]),
])
    
def test_set_event(neurons,input_string, expected):
    result = neurons.set_event(input_string)
    assert result == expected
    


@pytest.mark.parametrize("input_string, bce_value, expected", [
    ("pattern_a:pattern_a", a, [0,a]),
    ("pattern_b:event1", event1, [5, event1.average(b)]),
    ("pattern_c:event2", event2, [7, event2.average(c)]),
    ("pattern_c:event5", event2, [7, event2.average(c)]),
    ("event0:event3", event3, [6, event3.average(c)]),
    ("pattern_a:event6", event3, [7, event3.average(a)]),
])
def test_update_neuron_to_learn(neurons, input_string, bce_value, expected):
    neurons.set_event(input_string)
    result = neurons.update_neuron_to_learn(bce_value)
    assert result == expected




@pytest.mark.parametrize("arr_pattern, expected", [
    ( arr_patternes_bce, {'pattern_a': [0, a], 'pattern_b': [1,b], 'pattern_c': [2, c], 'pattern_d': [3, d], 'event0': [4, event.average(a)], 'event1': [5, event1.average(b)], 'event3': [6, event3.average(c)]}),
    ( arr_patternes_bce2, {'pattern_a': [0, a], 'pattern_b': [1,b], 'pattern_c': [2, c], 'pattern_d': [3, d], 'event0': [4, event.average(a)], 'event1': [5, event1.average(b)], 'event3': [6, event3.average(c)], "pattern_e" : [7,a], "pattern_f" : [8,b], "pattern_g" : [9,c], "pattern_h" : [10,d]}),
    
])

def test_get_neurons(neurons, arr_pattern, expected):
    neurons.init_patterns(arr_pattern)
    result = neurons.get_neurons()
    assert result == expected

def test_reset(neurons):
    neurons.reset()
    assert neurons.learned_neurons == {}
    assert neurons.neuron_to_learn == {}