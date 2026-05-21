############ Завдання a ############
def gen_xk(x):
    current_x = 1
    k = 0
    while True:
        yield current_x
        k += 1
        current_x *= x/(k*(k+1))

############ Завдання b ############
def gen_pn():
    current_p = 1
    i = 1
    fact_i = 1
    while True:
        fact_i *= i
        term = 2 + 1/fact_i
        current_p *= term
        yield current_p
        i += 1

############ Завдання c ############
def gen_Dc(a):
    d1 = a
    d2 = a**2-1
    yield d1
    yield d2
    while True:
        d_current = a*d2 - d1
        yield d_current
        d1, d2 = d2, d_current

############ Завдання d ############
def gen_sum():
    a1 = 1
    a2 = 1
    k = 1
    current_sum = 0
    fact_k = 1
    while True:
        if k > 1:
            fact_k *= k
        if k == 1:
            ak = a1
        elif k == 2:
            ak = a2
        else:
            ak = a2 + a1/2**k
            a1, a2 = a2, ak
        term = fact_k/ak
        current_sum += term
        yield current_sum
        k += 1

############ Завдання e ############
def gen_taylor_ln(x):
    term = x
    current_ln = term
    k = 1
    yield current_ln, term
    while True:
        term *= -x*k/(k+1)
        current_ln += term
        k += 1
        yield current_ln, term