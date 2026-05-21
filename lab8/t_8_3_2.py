############ Завдання a ############
def gen_xk(x):
    current_x = -x
    k = 1
    while True:
        yield current_x/k
        k += 1
        current_x *= -x

############ Завдання b ############
def gen_pn():
    current_p = 1
    i = 1
    while True:
        term = (i + 1) / (i + 2)
        current_p *= term
        yield current_p
        i += 1

############ Завдання c ############
def gen_Dc(x):
    d2 = 1 + x**2
    d1 = 1 + x**2 + x**4
    yield d1
    yield d2
    while True:
        d_current = (1 + x**2)*d1 - x**2*d2
        yield d_current
        d2, d1= d1, d_current
n = 4
generator_c = gen_Dc(2)
for _ in range(n):
    result_c = next(generator_c)
print(f"d{n} = {result_c}")

############ Завдання d ############
def gen_sum():
    a1 = 1
    a2 = 1
    k = 1
    current_sum = 0

    while True:
        if k == 1:
            ak = a1
        elif k == 2:
            ak = a2
        else:
            ak = a2/k + a1
            a1, a2 = a2, ak
        term = (3 ** k) / ak
        current_sum += term
        yield current_sum
        k += 1

############ Завдання e ############
def gen_taylor_ch(x):
    term = 1
    current_ch = term
    yield current_ch, term
    n = 1
    while True:
        term *= (x ** 2) / ((2 * n - 1) * (2 * n))
        current_ch += term
        yield current_ch, term
        n += 1