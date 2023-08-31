import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', 'src')
sys.path.append(src_dir)

from src.bce import BCE
from src.need import Need
import pytest
import random
import itertools
from src.intelligent_agent import Intelligent_agent


@pytest.fixture
def agent():
    return Intelligent_agent()

bce_samples=[]

for _ in range(100):
    index = _ % 4  # Ciclar entre 0, 1, 2, 3
    bce_samples.append([BCE().sample() for _ in range(index)])


def calculate_total_sum(bce_list):
    total_sum = BCE().zero()
    if len(bce_list) == 1:
        total_sum += bce_list[0]
        return total_sum
     
    for bce in bce_list:
        total_sum += bce
    return total_sum

cases=[]
for i,_ in enumerate(bce_samples):
    cases.append((bce_samples[i], calculate_total_sum(bce_samples[i])))

@pytest.mark.parametrize("bce_values, expected_status", cases)
def test_add_bce(agent, bce_values, expected_status):
    for bce_value in bce_values:
        agent.add_bce(bce_value)
    assert agent.status() == expected_status

def test_str_representation(agent):
    assert str(agent) == str(agent.status())

def test_repr_representation(agent):
    assert repr(agent) == str(agent.status())

possible_combinations = list(itertools.product([0, 1], range(4), repeat=6))
random_sample_1000 = random.sample(possible_combinations, 1000)

parameters_intelligent_agent_behavior = []
for need in possible_combinations:

    current_bce = BCE(Need(*need[0:2]), Need(*need[2:4]), Need(*need[4:6]))
    input_bce = BCE(Need(*need[6:8]), Need(*need[8:10]), Need(*need[10:12]))

    bce_resul=current_bce+input_bce
    

    ret_val=(current_bce,input_bce,bce_resul)
    parameters_intelligent_agent_behavior.append(ret_val)

@pytest.mark.parametrize("current_bce, input_bce, expected_status", parameters_intelligent_agent_behavior)
def test_intelligent_agent_behavior(agent, current_bce, input_bce, expected_status):
    agent.status_bce = current_bce
    agent.add_bce(input_bce)

    assert agent.status() == expected_status