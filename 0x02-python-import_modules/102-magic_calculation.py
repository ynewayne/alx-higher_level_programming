#!/usr/bin/python3
def magic_calculation(a, b):
    add = __import__('magic_calculation_102', globals(), locals(), ['add'], 0).add
    sub = __import__('magic_calculation_102', globals(), locals(), ['sub'], 0).sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
    else:
        c = sub(a, b)
        return c
