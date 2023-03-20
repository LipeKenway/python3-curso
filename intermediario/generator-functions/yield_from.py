"""
Yield from
"""
def gen1():
    print('Começou GEN 1')
    yield 1
    yield 2
    yield 3
    print('Acabou GEN 1')

def gen3():
    print('Começou GEN 3')
    yield 90
    yield 80
    yield 70
    print('Acabou GEN 3')


def gen2(gen=None):
    print('Começou GEN 2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('Acabou GEN 2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for numero in g1:
    print(numero)
print()

for numero in g2:
    print(numero)
print()

for numero in g3:
    print(numero)
print()
