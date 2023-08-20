import pytest
from itertools import product
from src.need import Need

LEN_DEGREE=4
len_sign=range(2)
len_degree=range(LEN_DEGREE)
sign=[1,-1]
sign_sub = [-1,1]
len_escalar=range(-4,LEN_DEGREE)


parameters_add = [
    (
        sign1,
        degree1,
        sign2,
        degree2,
        0 if val > 0 else 1 if val < 0 else sign1,
        min(abs(val), LEN_DEGREE),
    )
    for (sign1, degree1, sign2, degree2) in product(len_sign, len_degree, len_sign, len_degree)
    for val in [sign[sign1] * degree1 + sign[sign2] * degree2]
]


#print(parameters_add)

parameters_sub = [
    (
        sign1,
        degree1,
        sign2,
        degree2,
        0 if val > 0 else 1 if val < 0 else sign1,
        min(abs(val), LEN_DEGREE),
    )
    for (sign1, degree1, sign2, degree2) in product(len_sign, len_degree, len_sign, len_degree)
    for val in [sign[sign1] * degree1 + sign_sub[sign2] * degree2]
]

#print(parameters_sub)

parameters_mul = [
    (
        sign1,
        degree1,
        escalar,
        0 if val > 0 else 1 if val < 0 else sign1,
        min(abs(val), LEN_DEGREE),
    )
    for (sign1, degree1, escalar) in product(len_sign, len_degree, len_escalar)
    for val in [sign[sign1] * degree1 * escalar]
]

#print(parameters_mul)

parameters_div = [
    (
        sign1,
        degree1,
        escalar,
        0 if val > 0 else 1 if val < 0 else 1 if sign[sign1]*escalar<0 else 0,
        min(abs(val), LEN_DEGREE),
    )
    for (sign1, degree1, escalar) in product(len_sign, len_degree, len_escalar)
    if escalar != 0
    for val in [int(sign[sign1] * degree1 / escalar)]
]

#print(parameters_div)

parameters_lt = [
    (
        Need(sign1, degree1),
        Need(sign2, degree2),
        sign[sign1] < sign[sign2] if num1 == 0 and num2 == 0 else num1 < num2,
    )
    for (sign1, degree1, sign2, degree2) in product(len_sign, len_degree, len_sign, len_degree)
    for num1, num2 in [(sign[sign1] * degree1, sign[sign2] * degree2)]
]

#print(parameters_lt)

parameters_le = [
    (
        Need(sign1, degree1),
        Need(sign2, degree2),
        sign[sign1] <= sign[sign2] if num1 == 0 and num2 == 0 else num1 <= num2,
    )
    for (sign1, degree1, sign2, degree2) in product(len_sign, len_degree, len_sign, len_degree)
    for num1, num2 in [(sign[sign1] * degree1, sign[sign2] * degree2)]
]

#print(parameters_le)

parameters_eq = [
    (
        Need(sign1, degree1),
        Need(sign2, degree2),
        sign[sign1] == sign[sign2] if num1 == 0 and num2 == 0 else num1 == num2,
    )
    for (sign1, degree1, sign2, degree2) in product(len_sign, len_degree, len_sign, len_degree)
    for num1, num2 in [(sign[sign1] * degree1, sign[sign2] * degree2)]
]

#print(parameters_eq)

parameters_gt = [
    (
        Need(sign1, degree1),
        Need(sign2, degree2),
        sign[sign1] > sign[sign2] if num1 == 0 and num2 == 0 else num1 > num2,
    )
    for (sign1, degree1, sign2, degree2) in product(len_sign, len_degree, len_sign, len_degree)
    for num1, num2 in [(sign[sign1] * degree1, sign[sign2] * degree2)]
]

#print(parameters_gt)

parameters_ge = [
    (
        Need(sign1, degree1),
        Need(sign2, degree2),
        sign[sign1] >= sign[sign2] if num1 == 0 and num2 == 0 else num1 >= num2,
    )
    for (sign1, degree1, sign2, degree2) in product(len_sign, len_degree, len_sign, len_degree)
    for num1, num2 in [(sign[sign1] * degree1, sign[sign2] * degree2)]
]

#print(parameters_ge)

parameters_eq = [
    (
        Need(sign1, degree1),
        Need(sign2, degree2),
        sign[sign1] == sign[sign2] if num1 == 0 and num2 == 0 else num1 == num2,
    )
    for (sign1, degree1, sign2, degree2) in product(len_sign, len_degree, len_sign, len_degree)
    for num1, num2 in [(sign[sign1] * degree1, sign[sign2] * degree2)]
]

#print(parameters_eq)

parameters_ne = [
    (
        Need(sign1, degree1),
        Need(sign2, degree2),
        sign[sign1] != sign[sign2] if num1 == 0 and num2 == 0 else num1 != num2,
    )
    for (sign1, degree1, sign2, degree2) in product(len_sign, len_degree, len_sign, len_degree)
    for num1, num2 in [(sign[sign1] * degree1, sign[sign2] * degree2)]
]

#print(parameters_ne)

parameters_average = []
for sign1 in len_sign:
    for degree1 in len_degree:
        for sign2 in len_sign:
            for degree2 in len_degree:
                
             
                num1=sign[sign1]*degree1
                num2=sign[sign2]*degree2

                val=(num1+num2)//2
                expected_degree=abs(val) if abs(val)<=LEN_DEGREE else LEN_DEGREE
                
                if val == 0:
                    expected_sign = sign1
                elif val > 0:
                    expected_sign = 0
                else:
                    expected_sign = 1

               
                ret_val=(Need(sign1,degree1),Need(sign2,degree2),Need(expected_sign,expected_degree))
                parameters_average.append(ret_val)
                
#print(parameters_average)



# Prueba del método __add__
@pytest.mark.parametrize("sign1, degree1, sign2, degree2, expected_sign, expected_degree", parameters_add)
def test_add(sign1, degree1, sign2, degree2, expected_sign, expected_degree):
    need1 = Need(sign=sign1, degree=degree1)
    need2 = Need(sign=sign2, degree=degree2)
    need_sum = need1 + need2

    assert need_sum.state[0] == expected_sign
    assert need_sum.state[1] == expected_degree


# Prueba del método __sub__
@pytest.mark.parametrize("sign1, degree1, sign2, degree2, expected_sign, expected_degree", parameters_sub)
def test_subtract(sign1, degree1, sign2, degree2, expected_sign, expected_degree):
    need1 = Need(sign=sign1, degree=degree1)
    need2 = Need(sign=sign2, degree=degree2)
    need_diff = need1 - need2

    assert need_diff.state[0] == expected_sign
    assert need_diff.state[1] == expected_degree

# Prueba del método __mul__
@pytest.mark.parametrize("sign, degree, escalar, expected_sign, expected_degree", parameters_mul )

def test_multiply(sign, degree, escalar, expected_sign, expected_degree):
    need = Need(sign=sign, degree=degree)
    need_multiplied = need * escalar

    assert need_multiplied.state[0] == expected_sign
    assert need_multiplied.state[1] == expected_degree

# Prueba del método __truediv__
@pytest.mark.parametrize("sign, degree, escalar, expected_sign, expected_degree", parameters_div)
def test_divide(sign, degree, escalar, expected_sign, expected_degree):
    need = Need(sign=sign, degree=degree)
    need_divided = need / escalar

    assert need_divided.state[0] == expected_sign
    assert need_divided.state[1] == expected_degree

# Prueba del método __lt_operator__
@pytest.mark.parametrize("need1, need2, expected_result", parameters_lt)
def test_lt_operator(need1, need2, expected_result):

    assert (need1 < need2) == expected_result

# Prueba del método __le_operator__
@pytest.mark.parametrize("need1, need2, expected_result", parameters_le)
def test_le_operator(need1, need2, expected_result):
    assert (need1 <= need2) == expected_result

# Prueba del método __le_operator__
@pytest.mark.parametrize("need1, need2, expected_result", parameters_eq)
def test_eq_operator(need1, need2, expected_result):
    assert (need1 == need2) == expected_result

# Prueba del método __gt_operator__
@pytest.mark.parametrize("need1, need2, expected_result", parameters_gt)
def test_gt_operator(need1, need2, expected_result):
    assert (need1 > need2) == expected_result

# Prueba del método __ge_operator__
@pytest.mark.parametrize("need1, need2, expected_result", parameters_ge)
def test_ge_operator(need1, need2, expected_result):
    assert (need1 >= need2) == expected_result    

# Prueba del método __eq_operator__
@pytest.mark.parametrize("need1, need2, expected_result", parameters_eq)
def test_eq_operator(need1, need2, expected_result):
    assert (need1 == need2) == expected_result

# Prueba del método __ne_operator__
@pytest.mark.parametrize("need1, need2, expected_result", parameters_ne)
def test_ne_operator(need1, need2, expected_result):
    assert (need1 != need2) == expected_result

# Prueba del método average
@pytest.mark.parametrize("need1, need2, expected_result", parameters_average)
def test_average_method(need1, need2, expected_result):
    assert (need1.average(need2) ) == expected_result