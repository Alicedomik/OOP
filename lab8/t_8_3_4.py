############ Завдання a ############
def gen_xk(x):
    current_x = 1
    k = 0
    fact_k = 1
    while True:
        yield current_x / fact_k
        k += 1
        current_x *= -x
        start = (k - 1) ** 2 + (k - 1) + 1
        end = k ** 2 + k
        for i in range(start, end + 1):
            fact_k *= i


############ Завдання b ############
def gen_pn():
    current_p = 1
    i = 2
    while True:
        term = 1 - 1/i**2
        current_p *= term
        yield current_p
        i += 1

############ Завдання c ############
def gen_Dc():
    d1 = 1
    d2 = -2
    yield d1
    yield d2
    while True:
        d_current = 5 * d2 - 6 * d1
        yield d_current
        d1, d2 = d2, d_current

############ Завдання d ############
def gen_sum():
    a1 = 0
    a2 = 1
    k = 1
    current_sum = 0
    fact_k_minus_1 = 1
    fact_k= 1
    while True:
        if k > 1:
            fact_k *= k
        if k == 1:
            ak = a1
        elif k == 2:
            ak = a2
        else:
            fact_k_minus_1*= k-1
            ak = a2 + a1/fact_k_minus_1
            a1, a2 = a2, ak
        term = fact_k*ak
        current_sum += term
        yield current_sum
        k += 1

############ Завдання e ############
def gen_taylor(x):
    term = 1
    current = term
    yield current, term
    while True:
        term *= -x
        current += term
        yield current, term