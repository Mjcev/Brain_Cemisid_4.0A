import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', 'src')
sys.path.append(src_dir)

from src.bce import BCE
from src.need import Need
import numpy as np
import random
import itertools
import pytest


possible_combinations = list(itertools.product([0, 1], range(4), repeat=6))
random_sample_100 = random.sample(possible_combinations, 100)

parameters_bce_add = []
for need in random_sample_100:


    bio1 = Need(*need[0:2])
    cul1 = Need(*need[2:4])
    emo1 = Need(*need[4:6])
    bio2 = Need(*need[6:8])
    cul2 = Need(*need[8:10])
    emo2 = Need(*need[10:12])

    b_resul=bio1+bio2
    c_resul=cul1+cul2
    e_resul=emo1+emo2
    
    bce_resul=BCE(b_resul,c_resul,e_resul).state()
    ret_val=(bio1,cul1,emo1,bio2,cul2,emo2,bce_resul)
    parameters_bce_add.append(ret_val)

random_sample_100 = random.sample(possible_combinations, 100)

parameters_bce_eq = []
for need in random_sample_100:


    bio1 = Need(*need[0:2])
    cul1 = Need(*need[2:4])
    emo1 = Need(*need[4:6])
    bio2 = Need(*need[6:8])
    cul2 = Need(*need[8:10])
    emo2 = Need(*need[10:12])

    b_resul=bio1==bio2
    c_resul=cul1==cul2
    e_resul=emo1==emo2
    
    bce_resul=True if b_resul and c_resul and e_resul else False
    ret_val=(bio1,cul1,emo1,bio2,cul2,emo2,bce_resul)
    parameters_bce_eq.append(ret_val)


random_sample_100 = random.sample(possible_combinations, 100)

parameters_bce_average = []
for need in random_sample_100:


    bio1 = Need(*need[0:2])
    cul1 = Need(*need[2:4])
    emo1 = Need(*need[4:6])
    bio2 = Need(*need[6:8])
    cul2 = Need(*need[8:10])
    emo2 = Need(*need[10:12])

    b_resul=Need.average(bio1,bio2)
    c_resul=Need.average(cul1,cul2)
    e_resul=Need.average(emo1,emo2)
    
    bce_resul=BCE(b_resul,c_resul,e_resul).state()
    ret_val=(bio1,cul1,emo1,bio2,cul2,emo2,bce_resul)
    parameters_bce_average.append(ret_val)

@pytest.fixture
def bce():
    instance=BCE()
    return instance



@pytest.mark.parametrize(
    "biological1, cultural1, emotional1, biological2, cultural2, emotional2, expected_state",
    [
        (Need(0, 0), Need(0, 0), Need(0, 0), Need(0, 0), Need(0, 0), Need(0, 0), BCE(Need(0, 0), Need(0, 0), Need(0, 0)).state()),
        (Need(1, 3), Need(1, 2), Need(0, 0), Need(0, 1), Need(0, 2), Need(0, 3), BCE(Need(1, 2), Need(1, 0), Need(0, 3)).state()),
        (Need(0, 1), Need(0, 2), Need(0, 3), Need(1, 1), Need(1, 3), Need(1, 3), BCE(Need(0, 0), Need(1, 1), Need(0, 0)).state()),
        (Need(1, 0), Need(1, 0), Need(1, 0), Need(0, 0), Need(0, 0), Need(0, 0), BCE(Need(1, 0), Need(1, 0), Need(1, 0)).state()),
        (Need(1, 0), Need(1, 0), Need(1, 0), Need(0, 3), Need(0, 3), Need(0, 3), BCE(Need(0, 3), Need(0, 3), Need(0, 3)).state()),
        (Need(0, 2), Need(0, 2), Need(0, 2), Need(0, 2), Need(0, 2), Need(0, 2), BCE(Need(0, 4), Need(0, 4), Need(0, 4)).state()),
        (Need(1, 2), Need(1, 2), Need(1, 2), Need(1, 3), Need(1, 3), Need(1, 3), BCE(Need(1, 4), Need(1, 4), Need(1, 4)).state())
        # Agrega más casos de prueba aquí
    ]
)

def test_bce_add_manual(biological1, cultural1, emotional1, biological2, cultural2, emotional2, expected_state):
    bce1 = BCE(biological1, cultural1, emotional1)
    bce2 = BCE(biological2, cultural2, emotional2)

    bce_sum = bce1 + bce2

    assert np.array_equal(bce_sum.state(), expected_state)

@pytest.mark.parametrize("biological1, cultural1, emotional1, biological2, cultural2, emotional2, expected_state",parameters_bce_add)
def test_bce_add(biological1, cultural1, emotional1, biological2, cultural2, emotional2, expected_state):
    bce1 = BCE(biological1, cultural1, emotional1)
    bce2 = BCE(biological2, cultural2, emotional2)

    bce_sum = bce1 + bce2

    assert np.array_equal(bce_sum.state(), expected_state)


@pytest.mark.parametrize(
    "biological1, cultural1, emotional1, biological2, cultural2, emotional2, expected_state",
    [
        (Need(0, 0), Need(0, 0), Need(0, 0), Need(0, 0), Need(0, 0), Need(0, 0), True ),
        (Need(1, 3), Need(1, 2), Need(0, 0), Need(0, 1), Need(0, 2), Need(0, 3), False ),
        (Need(0, 1), Need(0, 2), Need(0, 3), Need(1, 1), Need(1, 3), Need(1, 3), False ),
        (Need(1, 0), Need(1, 0), Need(1, 0), Need(0, 0), Need(0, 0), Need(0, 0), False ),
        (Need(1, 0), Need(1, 0), Need(1, 0), Need(0, 3), Need(0, 3), Need(0, 3), False ),
        (Need(0, 2), Need(0, 2), Need(0, 2), Need(0, 2), Need(0, 2), Need(0, 2), True ),
        (Need(1, 2), Need(1, 2), Need(1, 2), Need(1, 3), Need(1, 3), Need(1, 3), False )
        # Agrega más casos de prueba aquí
    ]
)

def test_bce_eq_manual(biological1, cultural1, emotional1, biological2, cultural2, emotional2, expected_state):
    bce1 = BCE(biological1, cultural1, emotional1)
    bce2 = BCE(biological2, cultural2, emotional2)

    ret_val = bce1 == bce2

    assert np.array_equal(ret_val, expected_state)

@pytest.mark.parametrize("biological1, cultural1, emotional1, biological2, cultural2, emotional2, expected_state",parameters_bce_eq)
def test_bce_eq(biological1, cultural1, emotional1, biological2, cultural2, emotional2, expected_state):
    bce1 = BCE(biological1, cultural1, emotional1)
    bce2 = BCE(biological2, cultural2, emotional2)
    ret_val = bce1 == bce2

    assert np.array_equal(ret_val, expected_state)


@pytest.mark.parametrize(
    "biological1, cultural1, emotional1, biological2, cultural2, emotional2, expected_state",
    [
        (Need(1, 1), Need(1, 2), Need(1, 3), Need(0, 1), Need(0, 2), Need(0, 3), BCE(Need(1, 0), Need(1, 0), Need(1, 0)).state()),
        (Need(0, 0), Need(0, 0), Need(0, 0), Need(0, 0), Need(0, 0), Need(0, 0), BCE(Need(0, 0), Need(0, 0), Need(0, 0)).state()),
        (Need(1, 3), Need(1, 0), Need(0, 0), Need(1, 3), Need(1, 3), Need(0, 3), BCE(Need(1, 3), Need(1, 2), Need(0, 1)).state()),
        (Need(0, 4), Need(0, 0), Need(0, 0), Need(0, 10), Need(0, 0), Need(0, 0), BCE(Need(0, 4), Need(0, 0), Need(0, 0)).state()),
        # Agrega más casos de prueba aquí
    ]
)
def test_bce_average_manual(biological1, cultural1, emotional1, biological2, cultural2, emotional2, expected_state):
    bce1 = BCE(biological1, cultural1, emotional1)
    bce2 = BCE(biological2, cultural2, emotional2)

    bce_avg = BCE.average(bce1,bce2)

    assert np.array_equal(bce_avg.state(), expected_state)

@pytest.mark.parametrize("biological1, cultural1, emotional1, biological2, cultural2, emotional2, expected_state",parameters_bce_average)
def test_bce_average(biological1, cultural1, emotional1, biological2, cultural2, emotional2, expected_state):
    bce1 = BCE(biological1, cultural1, emotional1)
    bce2 = BCE(biological2, cultural2, emotional2)

    bce_avg = BCE.average(bce1,bce2)

    assert np.array_equal(bce_avg.state(), expected_state)