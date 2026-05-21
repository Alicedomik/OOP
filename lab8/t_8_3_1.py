import math

############ Завдання a ############
def gen_xk(x):
    current_x = x
    k = 1
    while True:
        yield current_x/k
        k += 1
        current_x = current_x * x

############ Завдання b ############
def gen_pn():
    current_p = 1
    i = 1
    while True:
        term = 1 / (i + math.factorial(1))
        current_p *= term
        yield current_p
        i += 1

############ Завдання c ############
def gen_Dc():
    d2 = 2
    d1 = 1
    yield d2
    yield d1
    while True:
        d_current = 2 * d1 - 3 * d2
        yield d_current
        d2, d1 = d1, d_current

############ Завдання d ############
def gen_sum():
    a1 = 0
    a2 = 1
    k = 1
    current_sum = 0

    while True:
        if k == 1:
            ak = a1
        elif k == 2:
            ak = a2
        else:
            ak = a2 + k * a1
            a1, a2 = a2, ak
        term = (2 ** k) * ak
        current_sum += term
        yield current_sum
        k += 1

############ Завдання e ############
def gen_taylor_sin(x):
    term = x
    current_sin = term
    n = 2
    yield current_sin, term
    while True:
        term = term * (-x ** 2) / ((2 * n - 2) * (2 * n - 1))
        current_sin += term
        yield current_sin, term
        n += 1