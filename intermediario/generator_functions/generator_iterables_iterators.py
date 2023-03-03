"""
Generator Expression, Iterables e Iterators em Python
"""
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem -> __iter__ e __next__

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

lista = [n for n in range(1, 11)]
generator = (n for n in range(1, 11))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# for n in generator:
#     print(n)


