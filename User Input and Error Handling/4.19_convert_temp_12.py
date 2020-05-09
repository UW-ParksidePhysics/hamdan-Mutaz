### Part c ###
from convert_temp import *
import sys

print(C2F(0), F2C(32), C2K(0), K2C(273.15), F2K(32), K2F(273.15))


def test_conversion():
    C = 0;
    F = 32;
    K = 273.15
    F_computed = C2F(F2C(F))
    C_computed = K2C(C2K(C))
    K_computed = K2F(F2K(F))

    def float_eq(a, b, tolerance=1e-14):
        float_eq = abs(a - b) < tolerance
        return float_eq

    success = float_eq(F_computed, F) and \
              float_eq(C_computed, C) and \
              float_eq(K_computed, F)
    msg = """Computations failed (correct answers in parenthesis):
    C=%g (%g)
    F=%g (%g)
    K=%g (%g)""" % (C_computed, C,
                    F_computed, F,
                    K_computed, F)
    assert success, msg


if len(sys.argv) == 2 and sys.argv[1] == 'test':
    print(test_conversion())
