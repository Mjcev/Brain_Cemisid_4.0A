import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', 'src')
sys.path.append(src_dir)

from src.bce import BCE
import pytest
from src.sensory_nn import Sensory_NN


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
def sensory_nn():
    instance=Sensory_NN("sight")
    arr_patternes_bce=[("pattern_a",a),("pattern_b",b),("pattern_c",c),("pattern_d",d)]
    instance.init_patterns(arr_patternes_bce)
    instance.set_event("pattern_a:event0")
    instance.update_neuron(event)
    instance.set_event("pattern_b:event1")
    instance.update_neuron(event1)
    instance.set_event("pattern_c:event3")
    instance.update_neuron(event3)
    return instance



@pytest.mark.parametrize("arr_pattern, expected", [
    ( arr_patternes_bce, [(0,"pattern_a_sight",a),(1,"pattern_b_sight",b),(2,"pattern_c_sight",c),(3,"pattern_d_sight",d)]),
    ( arr_patternes_bce2, [(7,"pattern_e_sight",a),(8,"pattern_f_sight",b),(9,"pattern_g_sight",c),(10,"pattern_h_sight",d)]),
])
def test_init_patterns(sensory_nn, arr_pattern, expected):
    result = sensory_nn.init_patterns(arr_pattern)
    assert result == expected


@pytest.mark.parametrize("event, bce_value, expected", [
    ("pattern_x", a, [7, a,"sight"]),
    ("pattern_y", b, [7, b,"sight"]),
    ("pattern_z", c, [7, c,"sight"])
])
def test_set_event_bce(sensory_nn, event, bce_value, expected):
    result = sensory_nn.set_event_bce(event, bce_value)
    assert result == expected


@pytest.mark.parametrize("input_string, expected", [
    ("pattern_a:pattern_a", [0,a,"sight"]),
    ("pattern_b:event1", [5, event1.average(b),"sight"]),
    ("pattern_c:event2", [7, c,"sight"]),
    ("pattern_c:event5", [7, c,"sight"]),
    ("event0:event3", [6, event3.average(c),"sight"]),
])
    
def test_set_event(sensory_nn,input_string, expected):
    result = sensory_nn.set_event(input_string)
    assert result == expected
    


@pytest.mark.parametrize("input_string, bce_value, expected", [
    ("pattern_a:pattern_a", a, [0,a,"sight"]),
    ("pattern_b:event1", event1, [5, event1.average(b),"sight"]),
    ("pattern_c:event2", event2, [7, event2.average(c),"sight"]),
    ("pattern_c:event5", event2, [7, event2.average(c),"sight"]),
    ("event0:event3", event3, [6, event3.average(c),"sight"]),
    ("pattern_a:event6", event3, [7, event3.average(a),"sight"]),
])
def test_update_neuron(sensory_nn, input_string, bce_value, expected):
    sensory_nn.set_event(input_string)
    result = sensory_nn.update_neuron(bce_value)
    assert result == expected

@pytest.mark.parametrize("arr_pattern, expected", [
    ( arr_patternes_bce, {'pattern_a_sight': [0, a], 'pattern_b_sight': [1,b], 'pattern_c_sight': [2, c], 'pattern_d_sight': [3, d], 'event0_sight': [4, event.average(a)], 'event1_sight': [5, event1.average(b)], 'event3_sight': [6, event3.average(c)]}),
    ( arr_patternes_bce2, {'pattern_a_sight': [0, a], 'pattern_b_sight': [1,b], 'pattern_c_sight': [2, c], 'pattern_d_sight': [3, d], 'event0_sight': [4, event.average(a)], 'event1_sight': [5, event1.average(b)], 'event3_sight': [6, event3.average(c)], "pattern_e_sight" : [7,a], "pattern_f_sight" : [8,b], "pattern_g_sight" : [9,c], "pattern_h_sight" : [10,d]}),
    
])

def test_status(sensory_nn, arr_pattern, expected):
    sensory_nn.init_patterns(arr_pattern)
    result = sensory_nn.status()
    assert result == expected

def test_reset(sensory_nn):
    sensory_nn.reset()
    assert sensory_nn.status() == {}